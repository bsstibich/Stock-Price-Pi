import yfinance as yf
from os import system, name
from time import sleep
from ticker_class import stock

def clear(): 						 
    if name == 'nt': # for windows
        _ = system('cls')  
    else: # for mac and linux
        _ = system('clear') 

gmeT = 'GME'
dogeT = 'DOGE-USD'
btcT = 'BTC-USD'
gme = stock(gmeT)

btc = stock(btcT)

doge = stock(dogeT)

while True:
    gme.get_prices()
    btc.get_prices()
    doge.get_prices()

    clear()

    
    
    gme.output()
    if(gme.current_price > gme.open_price):
        print("up")
    elif(gme.current_price < gme.open_price):
        print("down")
    else:
        print("neutral")

    btc.output()
    if(btc.current_price > btc.open_price):
        print("up")
    elif(btc.current_price < btc.open_price):
        print("down")
    else:
        print("neutral")

    doge.output()
    if(doge.current_price > doge.open_price):
        print("up")
    elif(doge.current_price < doge.open_price):
        print("down")
    else:
        print("neutral")
    
    sleep(40)


#while True:
#    gme = get_current_price(gmeT)
#    doge = get_current_price(dogeT)
#   btc = get_current_price(btcT)
#    os.system('cls')
#    print("GME: " + str(gme))
#    print("DOGE: " + str(doge))
#    print("BTC: " + str(btc))
#    sleep(30)