
import MetaTrader5 as mt5
import pandas as pd
import config

# --- FUNCTION: GET MOVING AVERAGES ---
def get_ma(symbol, timeframe, period):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, period+1)
    df = pd.DataFrame(rates)
    ma = df['close'].rolling(period).mean().iloc[-1]
    return ma

# --- FUNCTION: CHECK CROSSOVER ---
def mac_strategy(symbol=config.SYMBOL, timeframe=config.TIMEFRAME, fast_period=9, slow_period=21):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, slow_period+2)
    df = pd.DataFrame(rates)
    df['fast_ma'] = df['close'].rolling(fast_period).mean()
    df['slow_ma'] = df['close'].rolling(slow_period).mean()

    # fast MA just crossed above the slow MA
    if df['fast_ma'].iloc[-2] < df['slow_ma'].iloc[-2] and df['fast_ma'].iloc[-1] > df['slow_ma'].iloc[-1]:
        return "BUY"
    #fast MA just crossed below the slow MA
    elif df['fast_ma'].iloc[-2] > df['slow_ma'].iloc[-2] and df['fast_ma'].iloc[-1] < df['slow_ma'].iloc[-1]:
        return "SELL"
    else:
        return None