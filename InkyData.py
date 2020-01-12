#!/usr/bin/python3

import json
import requests
from time import sleep as s


price = float()
changed = float()

# values for ROI calculation
ca = 7030.50
inv = 2525.52
bv = inv / ca
pv = inv / 100
roi = float()

coin = '1720'
curr = 'EUR'

def coininfo():

    print('fetching data...')

    r = requests.get(
        'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=' + coin + '&convert=' + curr,
        headers={'X-CMC_PRO_API_KEY': '5451b6a0-06f7-4a7a-85b0-8bb65e28be74', 'Accept': 'application/json'})
    output = r.json()

#    rank = str(output['data'][coin]['cmc_rank'])
#    symbol = str(output['data'][coin]['symbol'])

    global price
    price = output['data'][coin]['quote'][curr]['price']

    global changed
    changed = output['data'][coin]['quote'][curr]['percent_change_24h']
    changedstr = str(changed)

    global roi
    roi = ca * price

    print('DATA LOADED')
