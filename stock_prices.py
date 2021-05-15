from ticker_class import Stock
from os import system, name
from time import sleep

def clear(): #CLI clear function					 
    if name == 'nt': # for windows
        _ = system('cls')  
    else: # for mac and linux
        _ = system('clear') 

#init stocks
gmeT = 'GME'
dogeT = 'DOGE-USD'
btcT = 'BTC-USD'
gme = Stock(gmeT)
btc = Stock(btcT)
doge = Stock(dogeT)

#running loop
try:
    while True:
        #get opening and current prices
        gme.get_prices()
        btc.get_prices()
        doge.get_prices()

        clear()

        #print current price
        gme.output()
        if(gme.current_price > gme.open_price):
            print("up")
        elif(gme.current_price < gme.open_price):
            print("down")
        else:
            print("neutral")
        sleep(20)
        gme.lcd_clear()

        #print current price
        btc.output()
        if(btc.current_price > btc.open_price):
            print("up")
        elif(btc.current_price < btc.open_price):
            print("down")
        else:
            print("neutral")
        sleep(20)
        btc.lcd_clear()
        
        
        #print current price
        doge.output()
        if(doge.current_price > doge.open_price):
            print("up")
        elif(doge.current_price < doge.open_price):
            print("down")
        else:
            print("neutral")
        sleep(20)
        doge.lcd_clear()    
except KeyboardInterrupt:
    btc.lcd_clear()
    btc.display.lcd_display_string("Stock Prices Pi",1)
    btc.display.lcd_display_string("Brandon Stibich v1.0",2)

