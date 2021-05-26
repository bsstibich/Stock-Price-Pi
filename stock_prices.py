from ticker_class import Stock
import led
from os import system, name
from time import sleep

def clear(): #CLI clear function					 
    if name == 'nt': # for windows
        _ = system('cls')  
    else: # for mac and linux
        _ = system('clear') 

def display_stock(stock):
        stock.lcd_clear()
        stock.output()
        try:
            if(stock.current_price > stock.open_price):
                print("up")
                led.green()
            elif(stock.current_price < stock.open_price):
                print("down")
                led.red()
            else:
                print("neutral")
                led.blue()
        except:
            stock.current_price = "PRICE ERROR"
            stock.open_price = "PRICE ERROR"
            print("PRICE ERROR")
            led.blue()
        sleep(5)

sleep(30)
#init stocks
gmeT = 'GME'
dogeT = 'DOGE-USD'
btcT = 'BTC-USD'
ethT = 'ETH-USD'
gme = Stock(gmeT)
btc = Stock(btcT)
doge = Stock(dogeT)
eth = Stock(ethT)
#init led
led.setup()

#running loop
while True:
    try:
        led.blue()
        gme.get_prices()
        btc.get_prices()
        doge.get_prices()
	eth.get_prices()

        clear()
        display_stock(gme)
        display_stock(btc)
        display_stock(doge)
	display_stock(eth)

    except KeyboardInterrupt:
        print("Shutting Down stock_prices.py")
        break
    finally:
        btc.lcd_clear()
        btc.display.lcd_display_string("Stock Prices Pi",1)
        btc.display.lcd_display_string("Brandon Stibich",2)
        led.blue()
led.destroy()
    


