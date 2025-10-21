import MetaTrader5 as mt5
import time
from strategies import rsi_strategy, mac_strategy, bollinger_strategy
from trading import place_order, initialize, close_prev_orders
from utils import percent_to_color
import config

initialize(login=config.login, server=config.server, password=config.password, path = config.path)

strategies = {
    "RSI": rsi_strategy,
    "MA": mac_strategy,
    "BOLL": bollinger_strategy
}

try:
    while True:
        votes = {"BUY": 0, "SELL": 0}
        total_strategies = len(strategies)

        for name, func in strategies.items():
            result = func()
            if result in votes:
                votes[result] += 1

        total_votes = sum(votes.values())
        if total_votes == 0:
            print(f"No clear signals, retrying in {config.SLEEP}s")
        else:
            # Majority signal and agreement percentage
            signal = max(votes, key=votes.get)
            percent = votes[signal] / total_strategies * 100
            color = percent_to_color(percent)
            reset = "\033[0m"
            agreeing = [name for name, func in strategies.items() if func() == signal]

            print(f"{color}Signal: {signal}, Agreement: {percent:.2f}% (Agreed: {', '.join(agreeing)}){reset}")
            if percent > 50:
                place_order(
                    config.SYMBOL,
                    mt5.ORDER_TYPE_BUY if signal == "BUY" else mt5.ORDER_TYPE_SELL,
                    config.LOT
                )
                close_prev_orders(signal)

        time.sleep(config.SLEEP)

except KeyboardInterrupt:
    print("Shutting down")
    mt5.shutdown()