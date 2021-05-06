#!/usr/bin/env python3
import requests
import json
import sys
import cryptocompare

coin = sys.argv[1]

cryptprice = cryptocompare.get_price(coin, currency="USDT")


temp = str(cryptprice.values())
a=temp.split()
b=str(a[1][:-3])


coin = coin.lower()+"inr"
val = b

url="https://api.wazirx.com/api/v2/trades?market={0}".format(coin)

response = requests.get(url).json()

for obj in response:
    price = obj['price']
    break

print(f'{coin} wazirx price is {price}')

url="https://api.wazirx.com/api/v2/trades?market=usdtinr"

response = requests.get(url).json()

for obj in response:
    price = obj['price']
    break

ogval = float(price) * float(val)

print(f'binance price is {ogval}')
