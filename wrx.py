#!/usr/bin/env python3
import requests
import json
import sys
coin = sys.argv[1]
try:
    cur = sys.argv[2]
    cur = 'usdt'
except:
    cur = 'inr'
coin = coin + cur
url="https://api.wazirx.com/api/v2/trades?market={0}".format(>
response = requests.get(url).json()
for obj in response:
    price = obj['price']
    print(f'{coin} price is {price}')
    break
