#!/usr/bin/env python3
import requests
import json
import sys
import cryptocompare
curd=""
coin = sys.argv[1]
price = 0
cur = ''
try:
    choice = sys.argv[2]
except:
    choice = 'i'

cryptprice = cryptocompare.get_price(coin, currency="USDT")

def getp(cry,cur):
    coin = cry  + cur
    url="https://api.wazirx.com/api/v2/trades?market={0}".for>
    response = requests.get(url).json()
    for obj in response:
        price = obj['price']
        break
    return price


temp = str(cryptprice.values())
a=temp.split()
b=str(a[1][:-3])


if choice == 'i':
    cur = 'inr'
    curd = '₹'
elif choice == 'u':
    cur = "usdt"
    curd = "$"
price = getp(coin,cur)

print()
print(f'__________ {coin} __________')
print()
print(f'wazirx price   : {curd}{price}')
wrx = price

price=1

if choice == 'i':
    price = getp('usdt','inr')

ogval = float(price) * float(b)
perc=((float(wrx)-ogval)/ogval)*100

print(f'binance price  : {curd}{ogval}')
print('difference     :  '+str(perc)[:7]+'%')
print('____________________________')
print()

