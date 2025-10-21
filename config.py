import MetaTrader5 as mt5

# --- CONFIG ---
SYMBOL = "EURUSD"
TIMEFRAME = mt5.TIMEFRAME_M1  # 1-minute bars
LOT = 0.01
RSI_PERIOD = 14
SLEEP = 60  # seconds
DAILY_TRADES = 5

# --- CONNECT TO MT5 ---
path = "C:/Program Files/MetaTrader 5/terminal64.exe"
login = 5040477202
server="MetaQuotes-Demo"
password="password"