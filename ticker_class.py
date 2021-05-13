import yfinance as yf
from yfinance import ticker

class stock():
    def __init__(self, ticker = ""):
    
        self.ticker = ticker
        self.open_price = self.get_open_price()
        self.current_price = self.get_current_price()

    def get_current_price(self):
        ticker = yf.Ticker(self.ticker)
        todays_data = ticker.history(period='1d')
        self.current_price = todays_data['Close'][0]
        return self.current_price
        
    
    def get_open_price(self):
        ticker = yf.Ticker(self.ticker)
        todays_data = ticker.history(period='1d')
        self.open_price = todays_data['Open'][0]
        return self.open_price
    
    def get_prices(self):
        self.get_open_price()
        self.get_current_price()
    
    def output(self):
        print(self.ticker + ": " + str(self.current_price))
