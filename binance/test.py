import ccxt
import telegram
import os
import time
from dotenv import load_dotenv
load_dotenv()

# Spot market
binance=ccxt.binance()

# Less frequent (daily)
listed_coin = []
for pair in binance.fetch_markets():
    if pair["quote"] == "USDT" and 'UP' not in pair["base"][-2:] and 'DOWN' not in pair["base"][-4:]:
        base_quote = "{}/{}".format(pair["base"], pair["quote"])
        listed_coin.append(base_quote)
        print("{} added".format(base_quote))

# More frequent (every minute, or every 30 secs)
start = time.perf_counter()
i = 0
binance_ticker = binance.fetch_tickers(listed_coin)
processed_data = []
for pair in binance_ticker.values():
    pair_data = {}
    pair_data["symbol"] = pair["symbol"]
    pair_data["price"] = pair["close"]
    pair_data["volume"] = pair["quoteVolume"]
    processed_data.append(pair_data)

print(processed_data)
end = time.perf_counter()
print(end - start)

'''
1. 거래소별 api써서 가격 긁어오기
2. if문으로 중복 코인을 비교하고 같은 페어끼리 가격을 비교

심화: 특정 거래소에서 가격 긁어오는게 에러 -> 이전 가격 쓰던지 아니면 스킵하던지

만약 이전 가격 쓰면 3회 이상 에러 -> 텔그로 노티

30초 간격으로 해서 2번 과정에서 이상치 발생하면 알림 보내기
'''