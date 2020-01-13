#!/usr/bin/python3

import json

class Configuration:

    def __init__(self, filename = "./config.json"):
        self.load(filename)

    def load(self, filename):

        with open(filename, 'r') as f:
            c = json.load(f)

            # API Key for your Coin Market Cap Account
            self.api_key = c["APIKey"]
            # ID of your Coin
            self.coin_id = c["CoinID"]
            # Currency for conversion
            self.currency = c["Currency"]
            # Investment in Fiat
            self.coin_invest = c["CoinInvest"]
            # Amount of tokens
            self.coin_amount = c["CoinAmount"]
            # Simple Mode on/off
            self.simple_mode = c["SimpleMode"]
            # Simple Personal Mode on/off
            self.simple_personal = c["SimplePersonal"]
            # Show ROI Label
            self.show_roi = c["ShowFiatROI"]
            # Background Image
            self.background = c["BackgroundImage"]
            # Background Portrait Mode
            self.back_simple = c["BackgroundSimple"]
            # Font Path
            self.font_path = c["FontPath"]
            # Set the color of your Inkyphat
            self.inky_color = c["InkyColor"]
            # Set border color
            self.inky_border_color = c["InkyBorderColor"]
            # Set Inky rotation
            self.inky_rotate = c["InkyRotate"]