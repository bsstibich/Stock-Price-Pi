import yfinance as yf
import os
from time import sleep

def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]
def get_open_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Open'][0]


while True:
    gme = get_current_price('GME')
    doge = get_current_price('DOGE-USD')
    btc = get_current_price('BTC-USD')
    os.system('cls')
    print("GME: " + str(gme))
    print("DOGE: " + str(doge))
    print("BTC: " + str(btc))
    sleep(30)