import yfinance as yf
from yfinance import ticker
import drivers

class Stock():
    def __init__(self, ticker = ""):
    
        self.ticker = ticker
        self.open_price = self.get_open_price()
        self.current_price = self.get_current_price()
        self.display = drivers.Lcd()

    def get_current_price(self):
        ticker = yf.Ticker(self.ticker) #yfinance ticker definition
        todays_data = ticker.history(period='1d') #get today's price history
        self.current_price = todays_data['Close'][0] #get most recent closing price
        return self.current_price
        
    
    def get_open_price(self):
        ticker = yf.Ticker(self.ticker) #yfinance ticker definition
        todays_data = ticker.history(period='1d') #get today's price history
        self.open_price = todays_data['Open'][0] #get today's opening price
        return self.open_price
    
    def get_prices(self): #update both current and open prices
        self.get_open_price()
        self.get_current_price()
    
    def output(self): #print current prices, will be adapted to LCD soon
        print(self.ticker + ": " + str(self.current_price))
        self.display.lcd_display_string("Hello World")

