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

        # Basic Inky settings
        inkyphat.set_colour(self.config.inky_color)
        inkyphat.set_border(self.config.inky_border_color)
        inkyphat.set_rotation(self.config.inky_rotate)

        # startup vars
        self.api_key = self.config.api_key
        self.coin_id = self.config.coin_id
        self.currency = self.config.currency
        self.coin_invest = self.config.coin_invest
        self.coin_amount = self.config.coin_amount
        self.show_roi = self.config.show_roi
        self.font = self.config.font_path

    # API call coinmarketcap.com and get the data needed for displaying
    def data(self):

        r = requests.get(
            'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=' + self.coin_id + '&convert=' + self.currency, headers={'X-CMC_PRO_API_KEY': self.api_key, 'Accept': 'application/json'})

        output = r.json()

        # write the vars with results from API call
        self.rank = str(output['data'][self.coin_id]['cmc_rank'])
        self.price = output['data'][self.coin_id]['quote'][self.currency]['price']
        self.day = output['data'][self.coin_id]['quote'][self.currency]['percent_change_24h']
        self.week = output['data'][self.coin_id]['quote'][self.currency]['percent_change_7d']

        self.roi = self.price * self.coin_amount

    # Set up mode 1
    def mode1(self):

        # background image
        img = Image.open(self.config.background)
        inkyphat.set_image(img)

        # Add the price text
        font = ImageFont.truetype(self.font, 36)
        price = str("%.3f" % self.price)
        inkyphat.text((4, 5), price, inkyphat.RED, font)

        # Add the day change text
        font = ImageFont.truetype(self.font, 22)
        day = "%.2f" % self.day
        if self.day > 0.0:
            inkyphat.text((7, 42), str(day), inkyphat.BLACK, font)
        if self.day < 0.0:
            inkyphat.text((7, 42), str(day), inkyphat.RED, font)

        # Add the ROI as FIAT
        if self.config.show_roi == True:

            font = ImageFont.truetype(self.font, 34)
            roi = self.price * self.coin_amount
            roistr = str("%.2f" % roi)
            inkyphat.text((4, 75), roistr, inkyphat.WHITE, font)

        # Add the ROI as percentage
        else:

            actual_value = self.price * self.coin_amount
            percentage = (actual_value / self.coin_invest * 100) - 100
            font = ImageFont.truetype(self.font, 34)
            roistr = str("%.2f" % percentage + '%')
            inkyphat.text((4, 75), roistr, inkyphat.WHITE, font)

        inkyphat.show()

    # Set up mode 2
    def mode2(self):

        # background image
        img = Image.open(self.config.back_simple)
        inkyphat.set_image(img)

        # Add ranking text
        font = ImageFont.truetype(self.font, 22)
        inkyphat.text((45, 5), "#" + self.rank, inkyphat.WHITE, font)

        # Add the price text
        font = ImageFont.truetype(self.font, 46)
        price = str("%.3f" % self.price)
        inkyphat.text((44, 25), price, inkyphat.WHITE, font)

        # Add the day change text
        font = ImageFont.truetype(self.font, 22)
        day = "%.2f" % self.day
        if self.day > 0.0:
            inkyphat.text((46, 62), "24h: " + str(day) + "%", inkyphat.WHITE, font)
        if self.day < 0.0:
            inkyphat.text((46, 62), "24h: " + str(day) + "%", inkyphat.RED, font)

        # Add the week change text
        font = ImageFont.truetype(self.font, 22)
        week = "%.2f" % self.week
        if self.week > 0.0:
            inkyphat.text((47, 82), "7d: " + str(week) + "%", inkyphat.WHITE, font)
        if self.week < 0.0:
            inkyphat.text((47, 82), "7d: " + str(week) + "%", inkyphat.RED, font)

        inkyphat.show()

    # Set up mode3
    def mode3(self):

        # background image
        img = Image.open(self.config.back_simple)
        inkyphat.set_image(img)

        # Add ranking text
        font = ImageFont.truetype(self.font, 22)
        inkyphat.text((45, 5), "#" + self.rank, inkyphat.WHITE, font)

        # Add the price text
        font = ImageFont.truetype(self.font, 48)
        price = str("%.3f" % self.price)
        inkyphat.text((44, 25), price, inkyphat.WHITE, font)

        # Add ROI Percentage
        actual_value = self.price * self.coin_amount
        percentage = (actual_value / self.coin_invest * 100) - 100
        font = ImageFont.truetype(self.font, 32)
        roistr = str("%.2f" % percentage + '%')
        if percentage > 0.0:
            inkyphat.text((44, 67), roistr, inkyphat.WHITE, font)
        else:
            inkyphat.text((44, 67), roistr, inkyphat.RED, font)

        inkyphat.show()
