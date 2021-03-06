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
        stock.get_prices()
        stock.lcd_clear()
        stock.output()
        try:
            if(stock.current_price > stock.open_price):
                led.green()
            elif(stock.current_price < stock.open_price):
                led.red()
            else:
                led.blue()
        except:
            stock.current_price = "PRICE ERROR"
            stock.open_price = "PRICE ERROR"
            print("PRICE ERROR")
            led.blue()
        sleep(2.5)

#sleep(30)
#init stocks

cook = Stock('COOK')
appl = Stock('AAPL')
spy = Stock('SPY')
negg = Stock('NEGG')
btc = Stock('BTC-USD')
doge = Stock('DOGE-USD')
eth = Stock('ETH-USD')
#init led
led.setup()
x = 0
#running loop
while True:
    try:
        led.blue()

        clear()
        display_stock(appl)
        display_stock(negg)
        display_stock(spy)
        display_stock(cook)
        display_stock(btc)
        display_stock(doge)
        display_stock(eth)

    except KeyboardInterrupt:
        print("Shutting Down stock_prices.py")
        break
    finally:
        sleep(2)
        btc.lcd_clear()
        btc.display.lcd_display_string("Stock Prices Pi",1)
        btc.display.lcd_display_string("Brandon Stibich",2)
        led.blue()
        x += 1
led.destroy()
print(f'Ran for {x} loops.')
    


