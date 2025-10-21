import MetaTrader5 as mt5
import pandas as pd
import config

# --- FUNCTION: GET RSI ---
def rsi_strategy(symbol=config.SYMBOL, timeframe=config.TIMEFRAME, period=config.RSI_PERIOD):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, period + 1)
    df = pd.DataFrame(rates)
    delta = df['close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(period).mean().iloc[-1]
    avg_loss = loss.rolling(period).mean().iloc[-1]
    rs = avg_gain / avg_loss if avg_loss != 0 else 0
    rsi = 100 - (100 / (1 + rs))
    
    if rsi < 30:
        return "BUY"
    elif rsi > 70:
        return "SELL"
    else:
        return "None"