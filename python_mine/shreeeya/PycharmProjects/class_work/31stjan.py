import json
from urllib.request import urlopen

with urlopen("https://api.coinmarketcap.com/v1/ticker/?limit=10") as response:
 source = response.read().decode('utf-8') # since, api responds with byte instead of char, we need to decode it

source_data = json.loads(source)

for coin in source_data:
 nam = (coin.get("name"))
 level = (coin.get("rank"))
 price = (coin.get("price_usd"))
 NPR = float(coin.get("price_usd")) * 100
 print(f"{nam}:{NPR}")
