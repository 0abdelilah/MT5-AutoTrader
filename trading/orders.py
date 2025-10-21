import MetaTrader5 as mt5
from trading import risk
import config


# --- FUNCTION: PLACE ORDER WITH SL/TP ---
def place_order(symbol, order_type, lot, rr_ratio=2.0):
    tick = mt5.symbol_info_tick(symbol)

    if tick is None:
        print("symbol_info_tick() failed, error code {}", mt5.last_error())
        return None

    atr = risk.get_atr(symbol, mt5.TIMEFRAME_M15)  # 15-min ATR

    #price = tick.ask if order_type == mt5.ORDER_TYPE_BUY else tick.bid

    if order_type == mt5.ORDER_TYPE_BUY:
        price = tick.ask
        sl = price - atr
        tp = price + (atr * rr_ratio)
    else:
        price = tick.bid
        sl = price + atr
        tp = price - (atr * rr_ratio)

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "magic": 123456,
        "symbol": symbol,
        "volume": lot,
        "type": order_type,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": 10,
        "comment": "Python RSI Bot",
        "type_filling": mt5.ORDER_FILLING_FOK
    }
    result = mt5.order_send(request)
    if result is None:
        print("order_send() failed, error code {}", mt5.last_error())
        return None
    print(result.comment)


# check all trades & close trade if opposite signal
def close_prev_orders(signal):
    positions = mt5.positions_get(symbol=config.SYMBOL)
    if positions and len(positions) > 0:
        for position in positions:
            prev_signal = "SELL" if position.type == 1 else "BUY"
            if signal != prev_signal:
                # close trade
                print(f"Strategies showing {signal}, Closing previous {prev_signal} trade")
                request = {
                    "action": mt5.TRADE_ACTION_DEAL,
                    "symbol": position.symbol,
                    "volume": position.volume,
                    "type": mt5.ORDER_TYPE_BUY if prev_signal == "SELL" else mt5.ORDER_TYPE_SELL,
                    "position": position.ticket,
                    "deviation": 20,
                    "magic": 234000,
                    "comment": "Close opposite trade"
                }
                mt5.order_send(request)
                print(f"Closed {prev_signal} trade with profit: ", position.profit)