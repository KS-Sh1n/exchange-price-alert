import ccxt
import time
import telegram

with open("./upbit.txt") as f:
        lines = f.readlines()
        api_key = lines[0].strip()
        api_secret = lines[1].strip()
        bot_token = lines[2].strip()
        bot_id = lines[3].strip()

upbit = ccxt.upbit(config={
    'apiKey': api_key,
    'secret': api_secret,
    'enableRateLimit': True
    }
)

bot = telegram.Bot(token = bot_token)


def upbit_get_market():
    listed_coin = []
    for pair in upbit.fetch_markets():
        if pair["quote"] == "USDT" and 'UP':
            base_quote = "{}/{}".format(pair["base"], pair["quote"])
            listed_coin.append(base_quote)
    return listed_coin

                                                        
def upbit_get_ticker(listed_coin):
                                                                
    upbit_ticker = upbit.fetch_tickers(listed_coin)

    processed_data = []
    for pair in upbit_ticker.values():
        pair_data = {}
        pair_data["symbol"] = pair["symbol"]
        pair_data["price"] = pair["close"]
        pair_data["volume"] = pair["quoteVolume"]
        processed_data.append(pair_data)                                   
    return processed_data
for i in range(3):
    time.sleep(20)
    tickers = upbit_get_ticker(upbit_get_market())
    bot.sendMessage(chat_id=bot_id, text = tickers)
