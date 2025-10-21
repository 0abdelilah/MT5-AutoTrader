# Simple Forex Trading Bot (MetaTrader 5 + Python)

This project is a **personal forex trading bot** built on **MetaTrader5 (MT5)** and **Python**.  
It starts as a simple RSI-based and progressively evolves into a multi-strategy trading system (bollinger bands, moving-averages)

## 🚀 Features

### 🎯 Core Trading
- **MetaTrader 5 integration** — Direct trade execution through MT5 API.  
- **Multi-strategy engine** — Supports multiple trading strategies:
  - RSI oversold/overbought entries.
  - Bollinger Bands for mean-reversion opportunities.
  - Moving Average crossover trend detection.
- **Adaptive scheduling** — Dynamic control of trade frequency and symbol scanning.

### 💰 Risk Management
- Configurable **max daily drawdown** and **stop trading on loss** rules.  
- Dynamic and trailing **stop-loss / take-profit** levels.  

## TODO

### 🧮 Analytics & Backtesting
- Offline backtesting with historical data  
- Performance metrics: win rate, profit factor, Sharpe ratio  
- Export logs/statistics (CSV/JSON)  
- Strategy comparison dashboard  

### 📰 News & Sentiment
- Integrate economic calendars (ForexFactory, Investing.com)  
- Pause trading during high-impact events  
- AI-driven sentiment analysis on news/headlines

## 📂 Project Structure
```
MT5-AutoTrader/
│
├── config.py               # Global configuration (symbols, lots, timeframes, etc.)
├── main.py                 # Entry point — runs the trading loop
├── README.md
├── requirements.txt
│
├── strategies/             # All trading strategy modules
│   ├── rsi.py              # RSI-based overbought/oversold logic
│   ├── macd.py             # MACD crossover momentum strategy (undone)
│   ├── bollinger.py        # Bollinger Bands mean reversion strategy
│   ├── mac.py              # Moving Average crossover strategy
│   └── __init__.py         # Package exports (import strategies cleanly)
│
├── trading/                # Core trading engine
│   ├── mt5_initialize.py   # MetaTrader 5 connection setup & shutdown
│   ├── orders.py           # Order execution logic (buy/sell)
│   ├── risk.py             # Risk and position sizing management
│   └── __init__.py         # Package exports for trading helpers
│
├── utils/                  # Shared utility modules
│   ├── utils.py            # Helper functions (indicators, logging, etc.)
│   └── __init__.py         # Package exports for utilities
│
```

## ⚙️ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/0abdelilah/MT5-AutoTrader
   cd forex-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up MetaTrader 5**
   - Install the MT5 desktop app and log into a **demo account**.
   - Keep MT5 running while using this bot.

4. **Run the bot**
   ```bash
   python main.py
   ```

## 📈 Disclaimer
This bot is for **educational and research purposes only**.
Trading forex involves significant risk of loss.
Always test using **demo accounts** before considering any live deployment.
