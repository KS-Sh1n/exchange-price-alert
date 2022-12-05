import ccxt
import json
import time

# Spot market
binance=ccxt.binance()

# Less frequently (daily)
def get_market_binance():
    listed_coin = []
    for pair in binance.fetch_markets():
        if pair["quote"] == "USDT" and 'UP' not in pair["base"][-2:] and 'DOWN' not in pair["base"][-4:]:
            base_quote = "{}/{}".format(pair["base"], pair["quote"])
            listed_coin.append(base_quote)

    with open("listed_coin_binance.json", "w") as f:
        f.writelines(listed_coin)

# More frequently (every minute, or every 30 secs)
def get_ticker_binance(listed_coin):
    # start = time.perf_counter()
    binance_ticker = binance.fetch_tickers(listed_coin)
    processed_data = []
    for pair in binance_ticker.values():
        pair_data = {}
        pair_data["symbol"] = pair["symbol"]
        pair_data["price"] = pair["close"]
        pair_data["volume"] = pair["quoteVolume"]
        processed_data.append(pair_data)
    processed_data = sorted(processed_data, key=lambda d: d["volume"], reverse=True)
    # end = time.perf_counter()
    # print(end - start)
    return processed_data

get_market_binance()