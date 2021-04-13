import requests
import json
import sys
coin = sys.argv[1]
url="https://api.wazirx.com/api/v2/trades?market={0}".format(coin)
response = requests.get(url).json()
for obj in response:
    price = obj['price']
    print(f'{coin} price is {price}')
    break
