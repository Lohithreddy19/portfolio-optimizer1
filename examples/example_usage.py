"""
Example: How to use the Portfolio Optimizer
"""

from src.portfolio_optimizer import PortfolioOptimizer

def main():
    # Define your portfolio stocks
    stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'JPM']
    
    # Create optimizer
    print("Creating Portfolio Optimizer...")
    optimizer = PortfolioOptimizer(
        symbols=stocks,
        start_date='2020-01-01',
        end_date='2024-01-01',
        risk_free_rate=0.02  # 2% risk-free rate
    )
    
    # Run optimization
    print("\nOptimizing portfolio...")
    results = optimizer.optimize()
    
    # Display results
    print("\n" + "="*60)
    print("PORTFOLIO OPTIMIZATION RESULTS")
    print("="*60)
    
    for strategy, data in results.items():
        print(f"\n{strategy.upper().replace('_', ' ')}:")
        print(f"  Expected Annual Return: {data['return']*100:.2f}%")
        print(f"  Annual Volatility (Risk): {data['volatility']*100:.2f}%")
        print(f"  Sharpe Ratio: {data['sharpe']:.2f}")
        print(f"  Asset Allocations:")
        for symbol, weight in data['weights'].items():
            print(f"    {symbol}: {weight*100:>5.2f}%")
    
    # Generate visualization
    print("\nGenerating efficient frontier plot...")
    optimizer.plot_efficient_frontier()
    print("\n✓ Done! Check docs/images/ folder for the plot.")

if __name__ == "__main__":
    main()
