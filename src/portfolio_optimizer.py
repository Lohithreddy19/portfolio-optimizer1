"""
Portfolio Optimizer - A tool for optimal asset allocation
"""

import numpy as np
import pandas as pd
import yfinance as yf
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple

class PortfolioOptimizer:
    """Portfolio optimization using Modern Portfolio Theory"""
    
    def __init__(self, symbols: List[str], start_date: str, end_date: str, 
                 risk_free_rate: float = 0.02):
        """
        Initialize the optimizer
        
        Args:
            symbols: List of stock ticker symbols (e.g., ['AAPL', 'MSFT'])
            start_date: Start date for historical data (format: 'YYYY-MM-DD')
            end_date: End date for historical data (format: 'YYYY-MM-DD')
            risk_free_rate: Annual risk-free rate (default: 0.02 = 2%)
        """
        self.symbols = symbols
        self.start_date = start_date
        self.end_date = end_date
        self.risk_free_rate = risk_free_rate
        self.returns = None
        self.mean_returns = None
        self.cov_matrix = None
        
    def fetch_data(self):
        """Download historical price data and calculate returns"""
        print(f"Downloading data for {', '.join(self.symbols)}...")
        
        # Download adjusted closing prices
        data = yf.download(self.symbols, start=self.start_date, 
                          end=self.end_date, progress=False)['Adj Close']
        
        # Handle single stock case
        if isinstance(data, pd.Series):
            data = data.to_frame(self.symbols[0])
        
        # Calculate daily returns
        self.returns = data.pct_change().dropna()
        
        # Annualize returns and covariance
        self.mean_returns = self.returns.mean() * 252
        self.cov_matrix = self.returns.cov() * 252
        
        print(f"✓ Downloaded {len(self.returns)} days of data")
        
    def portfolio_stats(self, weights: np.ndarray) -> Tuple[float, float, float]:
        """
        Calculate portfolio statistics
        
        Args:
            weights: Array of portfolio weights (must sum to 1)
            
        Returns:
            Tuple of (annual_return, annual_volatility, sharpe_ratio)
        """
        # Portfolio return
        portfolio_return = np.sum(self.mean_returns * weights)
        
        # Portfolio volatility (standard deviation)
        portfolio_std = np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix, weights)))
        
        # Sharpe ratio (risk-adjusted return)
        sharpe_ratio = (portfolio_return - self.risk_free_rate) / portfolio_std
        
        return portfolio_return, portfolio_std, sharpe_ratio
    
    def negative_sharpe(self, weights: np.ndarray) -> float:
        """Return negative Sharpe ratio (for minimization)"""
        return -self.portfolio_stats(weights)[2]
    
    def portfolio_volatility(self, weights: np.ndarray) -> float:
        """Return portfolio volatility"""
        return self.portfolio_stats(weights)[1]
    
    def optimize(self) -> Dict:
        """
        Find optimal portfolio allocations
        
        Returns:
            Dictionary with three portfolio strategies:
            - max_sharpe: Maximum Sharpe ratio (best risk-adjusted return)
            - min_volatility: Minimum volatility (lowest risk)
            - equal_weight: Equal allocation (benchmark)
        """
        if self.returns is None:
            self.fetch_data()
        
        num_assets = len(self.symbols)
        
        # Constraints: weights must sum to 1
        constraints = [{'type': 'eq', 'fun': lambda x: np.sum(x) - 1}]
        
        # Bounds: each weight between 0 and 1 (no short selling)
        bounds = tuple((0, 1) for _ in range(num_assets))
        
        # Initial guess: equal weights
        init_guess = np.array([1/num_assets] * num_assets)
        
        print("\nOptimizing portfolios...")
        
        # 1. Maximum Sharpe Ratio Portfolio
        opt_sharpe = minimize(
            self.negative_sharpe,
            init_guess,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )
        
        # 2. Minimum Volatility Portfolio
        opt_var = minimize(
            self.portfolio_volatility,
            init_guess,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )
        
        # 3. Equal Weight Portfolio (benchmark)
        equal_weights = np.array([1/num_assets] * num_assets)
        
        # Calculate statistics for each portfolio
        sharpe_stats = self.portfolio_stats(opt_sharpe.x)
        var_stats = self.portfolio_stats(opt_var.x)
        equal_stats = self.portfolio_stats(equal_weights)
        
        results = {
            'max_sharpe': {
                'weights': dict(zip(self.symbols, opt_sharpe.x)),
                'return': sharpe_stats[0],
                'volatility': sharpe_stats[1],
                'sharpe': sharpe_stats[2]
            },
            'min_volatility': {
                'weights': dict(zip(self.symbols, opt_var.x)),
                'return': var_stats[0],
                'volatility': var_stats[1],
                'sharpe': var_stats[2]
            },
            'equal_weight': {
                'weights': dict(zip(self.symbols, equal_weights)),
                'return': equal_stats[0],
                'volatility': equal_stats[1],
                'sharpe': equal_stats[2]
            }
        }
        
        print("✓ Optimization complete!")
        return results
    
    def plot_efficient_frontier(self, num_portfolios: int = 5000):
        """
        Plot the efficient frontier and optimal portfolios
        
        Args:
            num_portfolios: Number of random portfolios to generate
        """
        if self.returns is None:
            self.fetch_data()
        
        print(f"\nGenerating {num_portfolios} random portfolios...")
        
        # Generate random portfolios
        returns_list = []
        volatility_list = []
        sharpe_list = []
        
        for _ in range(num_portfolios):
            weights = np.random.random(len(self.symbols))
            weights /= np.sum(weights)
            
            ret, vol, sharpe = self.portfolio_stats(weights)
            returns_list.append(ret)
            volatility_list.append(vol)
            sharpe_list.append(sharpe)
        
        # Get optimal portfolios
        results = self.optimize()
        
        # Create plot
        plt.figure(figsize=(12, 8))
        
        # Plot random portfolios
        scatter = plt.scatter(volatility_list, returns_list, 
                            c=sharpe_list, cmap='viridis', 
                            alpha=0.5, s=10)
        plt.colorbar(scatter, label='Sharpe Ratio')
        
        # Plot optimal portfolios
        for name, portfolio in results.items():
            color = {'max_sharpe': 'red', 'min_volatility': 'green', 
                    'equal_weight': 'blue'}[name]
            label = {'max_sharpe': 'Max Sharpe Ratio', 
                    'min_volatility': 'Min Volatility',
                    'equal_weight': 'Equal Weight'}[name]
            
            plt.scatter(portfolio['volatility'], portfolio['return'],
                       marker='*', s=500, c=color, edgecolors='black',
                       label=label, linewidths=2, zorder=5)
        
        plt.xlabel('Volatility (Risk)', fontsize=12)
        plt.ylabel('Expected Annual Return', fontsize=12)
        plt.title('Efficient Frontier - Portfolio Optimization', 
                 fontsize=14, fontweight='bold')
        plt.legend(fontsize=10)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        # Save plot
        plt.savefig('docs/images/efficient_frontier.png', dpi=300, bbox_inches='tight')
        print("✓ Plot saved to docs/images/efficient_frontier.png")
        
        plt.show()


# Example usage
if __name__ == "__main__":
    # Define stocks to analyze
    stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'JPM']
    
    # Create optimizer
    optimizer = PortfolioOptimizer(
        symbols=stocks,
        start_date='2020-01-01',
        end_date='2024-01-01'
    )
    
    # Run optimization
    results = optimizer.optimize()
    
    # Print results
    print("\n" + "="*60)
    print("PORTFOLIO OPTIMIZATION RESULTS")
    print("="*60)
    
    for strategy, data in results.items():
        print(f"\n{strategy.upper().replace('_', ' ')}:")
        print(f"  Expected Return: {data['return']*100:.2f}%")
        print(f"  Volatility: {data['volatility']*100:.2f}%")
        print(f"  Sharpe Ratio: {data['sharpe']:.2f}")
        print(f"  Allocations:")
        for symbol, weight in data['weights'].items():
            print(f"    {symbol}: {weight*100:.2f}%")
    
    # Generate visualization
    optimizer.plot_efficient_frontier()
