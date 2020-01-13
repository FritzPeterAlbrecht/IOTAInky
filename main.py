#!/usr/bin/python3

from configuration import Configuration
from inkyticker import Inkyticker
from time import sleep

if __name__ == "__main__":

    # setup
    config = Configuration("/home/pi/PythonScripts/IOTAInky/config.json")
    ticker = Inkyticker(config)

    # run the programm
    sleep(10)
    ticker.data()
    if config.simple == True:
        ticker.simple()
    else:
        ticker.normal()