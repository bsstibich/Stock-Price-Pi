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
led.setup()

#running loop

while True:
    try:
        
        led.blue()
        gme.get_prices()
        btc.get_prices()
        doge.get_prices()


        clear()
        gme.lcd_clear()
        gme.output()
        try:
            if(gme.current_price > gme.open_price):
                print("up")
                led.green()
            elif(gme.current_price < gme.open_price):
                print("down")
                led.red()
            else:
                print("neutral")
                led.blue()
        except:
            gme.current_price = "PRICE ERROR"
            gme.open_price = "PRICE ERROR"
            led.blue()
        sleep(5)


        btc.lcd_clear()
        btc.output()
        try:
            if(btc.current_price > btc.open_price):
                print("up")
                led.green()
            elif(btc.current_price < btc.open_price):
                print("down")
                led.red()
            else:
                print("neutral")
                led.blue
        except:
            btc.current_price = "PRICE ERROR"
            btc.open_price = "PRICE ERROR"
            led.blue()
        sleep(5)
        
        
        doge.lcd_clear()
        doge.output()'
        try:
            if(doge.current_price > doge.open_price):
                print("up")
                led.green()
            elif(doge.current_price < doge.open_price):
                print("down")
                led.red()
            else:
                print("neutral")
                led.blue()
        except:
            doge.current_price = "PRICE ERROR"
            doge.open_price = "PRICE ERROR"
            led.blue()
        sleep(5)
    except KeyboardInterrupt:
        break
    finally:
        btc.lcd_clear()
        btc.display.lcd_display_string("Stock Prices Pi",1)
        btc.display.lcd_display_string("Brandon Stibich",2)
        led.blue()
led.destroy()    


