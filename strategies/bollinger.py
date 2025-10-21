import MetaTrader5 as mt5
import pandas as pd
import config

def get_bollinger(symbol=config.SYMBOL, timeframe=config.TIMEFRAME, period=20, deviation=2):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, period)
    df = pd.DataFrame(rates)
    df['ma'] = df['close'].rolling(period).mean()
    df['std'] = df['close'].rolling(period).std()
    df['upper'] = df['ma'] + deviation * df['std']
    df['lower'] = df['ma'] - deviation * df['std']
    return df['upper'].iloc[-1], df['ma'].iloc[-1], df['lower'].iloc[-1]

# --- FUNCTION: CHECK BOLLINGER SIGNAL ---
def bollinger_strategy():
    upper, middle, lower = get_bollinger()
    tick = mt5.symbol_info_tick(config.SYMBOL)
    price = tick.bid
    if price < lower:
        return "BUY"
    elif price > upper:
        return "SELL"
    else:
        return None
