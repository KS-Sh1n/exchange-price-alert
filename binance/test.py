import ccxt
import telegram
import os
import time
from dotenv import load_dotenv
load_dotenv()

# Spot market
binance=ccxt.binance()

listed_coin = []
for pair in binance.fetchMarkets():
    if pair['base'] not in listed_coin and 'UP' not in pair['base'][-2:] and 'DOWN' not in pair['base'][-4:]:
        listed_coin.append(pair['base'])
        print('{} added'.format(pair['base']))

# print(binance.fetch_ticker('{}/USDT'.format(listed_coin[0])))

start = time.perf_counter()
i = 0
binance_coins = []
for i in range(len(listed_coin)):
    try:
        binance_coin = {}
        binance_coin['symbol'] = listed_coin[i]
        binance_coin['price'] = binance.fetch_ticker('{}/USDT'.format(listed_coin[i]))['close']
        binance_coin['volume'] = binance.fetch_ticker('{}/USDT'.format(listed_coin[i]))['baseVolume']
        binance_coins.append(binance_coin)
        i = i + 1
        print('{} completed'.format(i))
    except:
        i = i + 1
        print('{} passed'.format(i))
        continue

print(len(binance_coins))
print(binance_coins)
end = time.perf_counter()
print(end - start)

'''
1. 거래소별 api써서 가격 긁어오기
2. if문으로 중복 코인을 비교하고 같은 페어끼리 가격을 비교

심화: 특정 거래소에서 가격 긁어오는게 에러 -> 이전 가격 쓰던지 아니면 스킵하던지

만약 이전 가격 쓰면 3회 이상 에러 -> 텔그로 노티

30초 간격으로 해서 2번 과정에서 이상치 발생하면 알림 보내기
'''