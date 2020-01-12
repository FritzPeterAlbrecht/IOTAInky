import json

class Configuration:

    def __init__(self, filename = "./config.json"):
        self.load(filename)

    def load(self, filename):

        with open(filename, 'r') as f:
            c = json.load(f)

            #print("loaded configuration: ", c)

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
            # Show ROI Label
            self.show_roi = c["ShowROI"]
            # Background Image
            self.background = c["BackgroundImage"]
            # Font Path
            self.font_path = c["FontPath"]
            # Set the color of your Inkyphat
            self.inky_color = c["InkyColor"]
            # Set border color
            self.inky_border_color = c["InkyBorderColor"]
            # Set Inky rotation
            self.inky_rotate = c["InkyRotate"]