### IOTAInky V0.1
IOTA Price Ticker for a RaspberryPi Zero WH and a Inkyphat e-Ink display

### Prerequisities

1 x Raspberry Pi Zero WH (https://shop.pimoroni.de/products/raspberry-pi-zero-wh-with-pre-soldered-header)

1 x Inkyphat (https://shop.pimoroni.de/products/inky-phat)

(as the code is written for the black and red version of the Inkyphat, you may adjust some lines if you choose a different color)

### Dependencies

In order to make IOTAInky work, you to install the some libraries.

Install the Inkyphat Python Library
```sh
$ sudo apt-get install python3-inkyphat
```

Also we need the requests package:
```sh
$ sudo pip3 install requests
```

#### Configuration file for the settings

| Setting | Function |
| ------- | -------- |
| APIKey | In order to make IOTAInky work, you need an account at https://coinmarketcap.com/api/ |
| CoinID | Coin ID from CMC you want to track |
| Currency | Currency conversion for example "USD", "GBP" or "BTC". There are many possible conversions |
| CoinInvest | To calculate the "return of investment" you need to set the amount of paid fiat |
| CoinAmount | The amount of your holdings (Tokens) to calculate ROI |
| SimpleMode | If set to true, IOTAInky is showing a slick black interface with no personal features like ROI |
| ShowFiatROI | "true" will show your ROI in Fiat, "false" shows it as percentage |
| BackgroundImage | Path to the background image |
| BackgroundSimple | Path to the background image for the simple mode |
| FontPath | Path to the used font - using a different font may destroy the positioning |
| InkyColor | General color of your Inkyphat - set to "yellow" for a yellow Inkyphat for example |
| InkyBorderColor | The border can be set to black or red, change it here |
| InkyRotate | Rotation of your Inkyphat |