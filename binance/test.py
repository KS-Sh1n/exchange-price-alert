import ccxt
import time

# Spot market
binance=ccxt.binance()

# Less frequent (daily)
def binance_get():
    listed_coin = []
    for pair in binance.fetch_markets():
        if pair["quote"] == "USDT" and 'UP' not in pair["base"][-2:] and 'DOWN' not in pair["base"][-4:]:
            base_quote = "{}/{}".format(pair["base"], pair["quote"])
            listed_coin.append(base_quote)
            print("{} added".format(base_quote))

    # More frequent (every minute, or every 30 secs)
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

