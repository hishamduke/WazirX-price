#!/usr/bin/env python3
import requests
import json
import sys
price = 2
def getp(arg):
    url="https://api.wazirx.com/api/v2/trades?market={0}".for>
    response = requests.get(url).json()
    for obj in response:
        price = obj['price']
        break
    return price

val = sys.argv[2]
coin = sys.argv[1]
wrx = getp(coin)

print()
print(f'__________ {coin} __________')
print()
print(f'wazirx price   :  {wrx}')

usdt = getp('usdtinr')
ogval = float(usdt) * float(val)

perc=((float(wrx)-ogval)/ogval)*100

print(f'binance price  :  {ogval}')
print('difference     :  '+str(perc)[:7]+'%')
print('____________________________')
print()
