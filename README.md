# Algorithmic Trading Strategies – Backtesting with Python

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![backtesting.py](https://img.shields.io/badge/backtesting.py-0.3.3-green.svg)](https://github.com/kernc/backtesting.py)
[![pandas](https://img.shields.io/badge/pandas-1.5.0-red.svg)](https://pandas.pydata.org/)
[![YouTube](https://img.shields.io/badge/YouTube-Playlist-red.svg)](https://youtube.com/playlist?list=PLvP9VMC55awTm6bsvfDt87DxIuISGf_Zf&si=6JNEgVElY5LRWmyw)

**Learn algorithmic trading by building strategies from scratch.**
**Backtest, optimize, and deploy your own trading bots.**

[📺 Watch the Full YouTube Playlist](https://youtube.com/playlist?list=PLvP9VMC55awTm6bsvfDt87DxIuISGf_Zf&si=6JNEgVElY5LRWmyw) • 
[🚀 Try Our Platform](https://algotradium.com)

</div>

---

## 📌 Overview

This repository contains complete, production-ready Python code for **backtesting trading strategies** using the `backtesting.py` library. Each strategy is implemented as a self-contained class and includes:

- ✅ **Custom indicators** (built from scratch – no black boxes)
- ✅ **Stop loss & take profit** (professional risk management)
- ✅ **Parameter optimization** (find the best settings automatically)
- ✅ **Ready to deploy** (copy-paste into any Python environment)

All code is explained step-by-step in the accompanying **YouTube playlist**. You can run these notebooks locally, or paste them directly into **[our platform](https://algotradium.com)** to backtest, create Telegram signal bots, and sell your strategies on the marketplace.

---

<!-- ## 📂 Repository Structure -->


---

## 🎯 What You'll Learn

| Video | Strategy | Skills |
| :--- | :--- | :--- |
| **#1** | SMA Crossover | Basic backtesting, equity curves, trade analysis |
| **#2** | RSI + MACD | Multiple indicators, pandas-ta, CSV data loading |
| **#3** | SL/TP | Risk management, position sizing, exit conditions |
| **#4** | Parameter Optimization | Grid search, heatmaps, preventing overfitting |
| **#5** | Custom RSI | Build indicators from scratch, no external libraries |
| **#6** | Ichimoku Cloud | Multi-component indicators, advanced entry/exit logic |

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/quant-riyan/backtest-trading-strategies-with-python--codes.git
```


## 📺 YouTube Playlist

All code in this repository is explained step-by-step in my YouTube playlist:

[**Click here to watch the full playlist**](https://youtube.com/playlist?list=PLvP9VMC55awTm6bsvfDt87DxIuISGf_Zf&si=6JNEgVElY5LRWmyw)

The videos cover:
- Create simple to complicated trading strategies with stop-loss and take-profit
- Optimize your strategy for maximum return or sharpe ratio
- How to code custom indicators
- The mathematical formula behind each indicator
- Step-by-step coding in VS Code / Jupyter
- Backtest results and interpretation
- How to deploy the strategy as a Telegram bot
- How to sell your strategy on our marketplace

---

## 🚀 Deploy Your Strategies

Once you have backtested and validated your strategy, you can:

### Option 1: Run locally
Keep using the code as-is in your own Python environment.

### Option 2: Use our platform
Copy-paste your strategy class into **[our platform](https://algotradium.com)** and get:

- **Unlimited backtests** on forex & crypto (daily timeframe is free)
- **One-click Telegram signal bots** – run 24/7, no server needed (for subscribed users only)
- **Live performance monitoring** – track your bot's win rate, drawdown, and trades history in real-time
- **Marketplace** – buy other quants advanced strategies and receive signals

👉 **[Start for free](https://algotradium.com)** – no credit card required.

---

## 📦 Dependencies

Create a `requirements.txt` file with:

```bash
backtesting==0.3.3
pandas==1.5.3
numpy==1.24.3
matplotlib==3.7.1
pandas-ta==0.3.14b0
yfinance==0.2.28
jupyter==1.0.0
```

Install all dependencies with:

```bash
pip install -r requirements.txt
```
## 📁 Sample Data Format

Your CSV file should have the following columns (some sample data are available in the Data folder):

| Date | Open | High | Low | Close | Volume |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2020-01-01 | 7200.5 | 7300.2 | 7150.0 | 7250.3 | 1000000 |
| 2020-01-02 | 7250.3 | 7400.1 | 7230.0 | 7380.5 | 1200000 |

You can download free historical data from:
- Yahoo Finance (using `yfinance` library)
- Binance (crypto)
- FXCM (forex)

---

## 🤝 Contributing

Found a bug or have an improvement? Feel free to reach me at support@algotradium.com.

---

## 📬 Connect with Me

- 📺 **YouTube**: [Riyan](https://youtube.com/@QuantRiyan)
<!-- - 💬 **Discord**: [Join our community](https://discord.gg/yourinvite) -->
- 🚀 **Platform**: [algotradium.com](https://algotradium.com)

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

**Happy backtesting!**

</div>