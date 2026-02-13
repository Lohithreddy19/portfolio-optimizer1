# 📊 Portfolio Optimizer

A Python-based portfolio optimization tool implementing Modern Portfolio Theory (MPT) to find optimal asset allocations.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🎯 Features

- **Efficient Frontier Calculation** - Find optimal risk-return tradeoffs
- **Multiple Optimization Strategies** - Max Sharpe, Min Volatility, Equal Weight
- **Real-Time Data** - Fetch historical prices from Yahoo Finance
- **Interactive Visualizations** - Beautiful charts and plots
- **Risk Metrics** - Sharpe ratio, volatility, correlation analysis

## 🚀 Quick Start

### Installation
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/portfolio-optimizer.git
cd portfolio-optimizer

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage
```python
from src.portfolio_optimizer import PortfolioOptimizer

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

# Visualize efficient frontier
optimizer.plot_efficient_frontier()
```

## 📊 Example Output
```
MAXIMUM SHARPE RATIO PORTFOLIO:
  Expected Return: 18.5%
  Volatility: 15.2%
  Sharpe Ratio: 1.22
  Allocations:
    AAPL: 25.3%
    MSFT: 32.1%
    GOOGL: 18.7%
    AMZN: 15.2%
    JPM: 8.7%
```

## 🛠️ Technologies Used

- **Python 3.8+**
- **pandas & numpy** - Data manipulation and analysis
- **scipy** - Optimization algorithms
- **yfinance** - Stock market data
- **matplotlib & plotly** - Data visualization

## 📚 Theory Background

This project implements **Modern Portfolio Theory** developed by Harry Markowitz:

- **Diversification reduces risk** - Don't put all eggs in one basket
- **Optimal portfolios** balance risk and return
- **Sharpe Ratio** measures risk-adjusted performance

### Key Formulas

**Expected Portfolio Return:**
```
E(Rp) = Σ(wi × E(Ri))
```

**Portfolio Variance:**
```
σ²p = Σ Σ(wi × wj × Cov(Ri, Rj))
```

**Sharpe Ratio:**
```
SR = (E(Rp) - Rf) / σp
```

## 📖 Project Structure
```
portfolio-optimizer/
├── src/
│   └── portfolio_optimizer.py    # Main optimization code
├── examples/
│   └── example_usage.py          # Usage examples
├── tests/
│   └── test_optimizer.py         # Unit tests
├── docs/
│   └── images/                   # Visualizations
├── requirements.txt              # Dependencies
└── README.md                     # This file
```

## 🔮 Future Enhancements

- [ ] Add Monte Carlo simulation
- [ ] Implement backtesting framework
- [ ] Support for cryptocurrency portfolios
- [ ] Web dashboard interface
- [ ] Machine learning predictions
- [ ] Risk parity strategy

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📧 Contact

Your Name - [@yourhandle](https://twitter.com/yourhandle)

Project Link: [https://github.com/YOUR_USERNAME/portfolio-optimizer](https://github.com/YOUR_USERNAME/portfolio-optimizer)

---

**⭐ Star this repository if you find it helpful!**
```

4. **Replace `YOUR_USERNAME`** with your actual GitHub username
5. **Scroll down and click "Commit changes"**

#### B) Create requirements.txt

1. **Click "Add file"** → **"Create new file"**
2. **Name it:** `requirements.txt`
3. **Paste this:**
```
pandas>=1.3.0
numpy>=1.21.0
scipy>=1.7.0
yfinance>=0.1.70
matplotlib>=3.4.0
plotly>=5.3.0
seaborn>=0.11.0
jupyter>=1.0.0
