# Methodology

## Modern Portfolio Theory (MPT)

This project implements Modern Portfolio Theory, developed by Harry Markowitz in 1952, for which he won the Nobel Prize in Economics in 1990.

## Core Concepts

### 1. Expected Portfolio Return

The expected return of a portfolio is the weighted average of expected returns of individual assets:
```
E(Rp) = Σ(wi × E(Ri))
```

Where:
- `wi` = weight of asset i in the portfolio
- `E(Ri)` = expected return of asset i
- `Σ` = sum across all assets

### 2. Portfolio Risk (Volatility)

Portfolio variance considers both individual asset volatility and correlations between assets:
```
σ²p = Σ Σ(wi × wj × Cov(Ri, Rj))
```

Where:
- `Cov(Ri, Rj)` = covariance between returns of assets i and j
- `σp` = √(σ²p) = portfolio standard deviation (volatility)

### 3. Sharpe Ratio

The Sharpe ratio measures risk-adjusted returns:
```
Sharpe Ratio = (E(Rp) - Rf) / σp
```

Where:
- `Rf` = risk-free rate (e.g., Treasury bill rate)
- Higher Sharpe ratio = better risk-adjusted performance

## Optimization Strategies

### Maximum Sharpe Ratio Portfolio

Finds the portfolio with the highest risk-adjusted return. This is typically recommended for most investors as it provides the best "bang for your buck" in terms of return per unit of risk.

### Minimum Volatility Portfolio

Finds the portfolio with the lowest possible risk (volatility). Suitable for very risk-averse investors who prioritize capital preservation.

### Equal Weight Portfolio

Simple benchmark where each asset gets equal allocation (1/N for N assets). Often used as a comparison baseline.

## Efficient Frontier

The efficient frontier is the set of optimal portfolios that offer:
- Maximum expected return for a given level of risk, OR
- Minimum risk for a given level of expected return

All portfolios on the efficient frontier are "efficient" - you cannot improve return without taking more risk, or reduce risk without accepting lower returns.

## Assumptions

1. **Returns are normally distributed** - In reality, markets have fat tails
2. **Investors are risk-averse** - They prefer less risk for the same return
3. **Historical data predicts future** - Past performance ≠ future results
4. **No transaction costs** - Real trading has costs and taxes
5. **Perfect information** - All investors have access to same data

## Limitations

- Sensitive to estimation errors in expected returns and covariances
- Assumes constant correlations (they change during crises)
- Ignores market microstructure, liquidity, and trading costs
- Based on historical data which may not repeat

## Practical Considerations

When using this tool:
- Use at least 2-3 years of historical data
- Rebalance portfolios periodically (quarterly or annually)
- Consider transaction costs in real implementations
- Diversify across asset classes, not just individual stocks
- Combine with fundamental analysis, not just quantitative optimization
