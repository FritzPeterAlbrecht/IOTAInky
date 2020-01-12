#!/usr/bin/python3

import inkyphat
from PIL import Image
from PIL import ImageFont
import json
import requests
from time import sleep as s


class Inkyticker:

    def __init__(self, config):

        self.config = config

        # basic settings of the inkyphat
        inkyphat.set_colour(self.config.inky_color)
        inkyphat.set_border(self.config.inky_border_color)
        inkyphat.set_rotation(self.config.inky_rotate)
        inkyphat.set_image(self.config.background)

        # startup vars
        api_key = self.config.api_key
        coin_id = self.config.coin_id
        currency = self.config.currency
        coin_invest = self.config.coin_invest
        self.coin_amount = self.config.coin_amount
        show_roi = self.config.show_roi
        self.font = self.config.font_path

    # API call coinmarketcap.com and get the data needed for displaying
    def data(self):

        r = requests.get(
            'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=' + coin_id + '&convert=' + currency, header={'X-CMC_PRO_API_KEY': '5451b6a0-06f7-4a7a-85b0-8bb65e28be74', 'Accept': 'application/json'})

        output = r.json()

        # write the vars with results from API call
        self.price = output['data'][coin_id]['quote'][currency]['price']
        self.day = output['data'][coin_id]['quote'][currency]['percent_change_24h']
        self.week = output['data'][coin_id]['quote'][currency]['percent_change_7d']

        self.roi = self.price * self.coin_amount

    # Set the different parts for the Inkyphat
    def controller(self):

        # Add the price text
        font = ImageFont.truetype(self.font, 36)
        price = str("%.3f" % self.price)
        print(price)
        inkyphat.text((4, 5), price, inkyphat.RED, font)

        # Add the day change text
        font = ImageFont.truetype(self.font, 22)
        day = "%.2f" % self.day
        if changed >= 0.0:
            inkyphat.text((7, 42), day, inkyphat.BLACK, font)
        if changed <= 0.0:
            inkyphat.text((7, 42), day, inkyphat.RED, font)

        # Add the ROI text
        font = ImageFont.truetype(self.font, 34)
        roi = self.price * self.config.coin_amount
        roistr = str(roi)

        inkyphat.text((4, 75), roistr[0:7], inkyphat.WHITE, font)

        inkyphat.show()