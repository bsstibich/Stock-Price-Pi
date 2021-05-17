from ticker_class import Stock
import led
from os import system, name
from time import sleep

def clear(): #CLI clear function					 
    if name == 'nt': # for windows
        _ = system('cls')  
    else: # for mac and linux
        _ = system('clear') 
sleep(30)
#init stocks
gmeT = 'GME'
dogeT = 'DOGE-USD'
btcT = 'BTC-USD'
gme = Stock(gmeT)
btc = Stock(btcT)
doge = Stock(dogeT)

#running loop

while True:
    try:
        
        clear()
        gme.get_prices()
        btc.get_prices()
        doge.get_prices()
        #print current price
        
        gme.lcd_clear()
        gme.output()
        if(gme.current_price > gme.open_price):
            print("up")
            led.green()
        elif(gme.current_price < gme.open_price):
            print("down")
            led.red()
        else:
            print("neutral")
            led.blue()
        sleep(5)
        

        #print current price
        
        btc.lcd_clear()
        btc.output()
        if(btc.current_price > btc.open_price):
            print("up")
            led.green()
        elif(btc.current_price < btc.open_price):
            print("down")
            led.red()
        else:
            print("neutral")
            led.blue
        sleep(5)
        
        
        #print current price
        
        doge.lcd_clear()
        doge.output()
        if(doge.current_price > doge.open_price):
            print("up")
            led.green()
        elif(doge.current_price < doge.open_price):
            print("down")
            led.red()
        else:
            print("neutral")
            led.blue()
        sleep(5)
    except KeyboardInterrupt:
        break
    finally:
        btc.lcd_clear()
        btc.display.lcd_display_string("Stock Prices Pi",1)
        btc.display.lcd_display_string("Brandon Stibich",2)
    


