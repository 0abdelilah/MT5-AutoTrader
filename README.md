Trader — Algorithmic trading helpers for MetaTrader5

Overview

This repository contains small Python utilities and trading strategy modules intended to help automate trading on MetaTrader 5 (MT5). It includes initialization and order helpers, basic risk-management utilities, and several example strategies (RSI, MACD, Bollinger, etc.). The code is lightweight and intended as a starting point for building and testing algorithmic strategies with MT5.

Contents

- `main.py` — Entry script (example runner) that ties initialization and strategy execution together.
- `config.py` — Configuration constants and settings used across the project.
- `trading/mt5_initialize.py` — MT5 connection/initialization helpers.
- `trading/orders.py` — Order placement and wrapper functions for interacting with MT5.
- `trading/risk.py` — Risk management utilities (position sizing, stop-loss/take-profit helpers).
- `strategies/` — Example strategy modules:
  - `rsi.py` — RSI-based entry/exit logic.
  - `macd.py` — MACD-based strategy.
  - `mac.py` — Moving-average crossover strategy.
  - `bollinger.py` — Bollinger Bands strategy.
- `utils/utils.py` — Small helper functions used by strategies and trading modules.

Quickstart

1. Create and activate a Python virtual environment (recommended):

   powershell
   python -m venv .venv; .\.venv\Scripts\Activate.ps1

2. Install dependencies (create `requirements.txt` if not present):

   pip install -r requirements.txt

   Suggested packages (if you don't have a `requirements.txt` yet):
   - MetaTrader5
   - pandas
   - numpy
   - pytz

3. Configure `config.py` with your MT5 account details and preferences.

4. Initialize MT5 and run the example in `main.py`:

   python main.py

Notes

- This project assumes you have MT5 installed and a valid account configured.
- Use a demo account while testing automated strategies.
- Review and adjust risk settings in `trading/risk.py` before using live funds.

Troubleshooting

- "Failed to initialize MT5": check that MT5 is installed and the account details in `config.py` are correct.
- "ModuleNotFoundError" or missing dependencies: install packages from `requirements.txt` or see the Suggested packages list above.

License

Add your license information here (e.g., MIT).