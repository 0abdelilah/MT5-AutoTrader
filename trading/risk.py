import MetaTrader5 as mt5
import pandas as pd

# --- FUNCTION: GET ATR ---
def get_atr(symbol, timeframe, period=14):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, period+1)
    df = pd.DataFrame(rates)

    df['high_low'] = df['high'] - df['low']
    df['high_close'] = abs(df['high'] - df['close'].shift())
    df['low_close'] = abs(df['low'] - df['close'].shift())
    df['tr'] = df[['high_low', 'high_close', 'low_close']].max(axis=1)
    atr = df['tr'].rolling(period).mean().iloc[-1]
    return atr