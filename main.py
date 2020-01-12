from configuration import Configuration
from inkyticker import Inkyticker
from time import sleep

if __name__ == "__main__":

    # setup
    config = Configuration("/home/pi/PythonScripts/crypticV4/CrypticV4.0config.json")
    ticker = Inkyticker(config)

    # run the programm
    #sleep(10)
    ticker.data()
    #sleep(2)
    ticker.controller()