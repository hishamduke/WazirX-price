#!/usr/bin/env python3
import requests
import json
import sys
import cryptocompare

coin = sys.argv[1]
try:
    choice = sys.argv[2]
except:
    choice = 'i'
cryptprice = cryptocompare.get_price(coin, currency="USDT")

temp = str(cryptprice.values())
a=temp.split()
b=str(a[1][:-3])

if choice == 'i':
    coin = coin.lower()+"inr"
elif choice == 'u':
    coin = coin.lower()+"usdt"

val = b

url="https://api.wazirx.com/api/v2/trades?market={0}".format(coin)

response = requests.get(url).json()

for obj in response:
    price = obj['price']
    break

print()
print(f'__________ {coin} __________')
print()
print(f'wazirx price   :  {price}')


price=1

if choice == 'i':
    url="https://api.wazirx.com/api/v2/trades?market=usdtinr"
    response = requests.get(url).json()
    for obj in response:
        price = obj['price']
        break

ogval = float(price) * float(val)

print(f'binance price  :  {ogval}')
print('____________________________')
print()

