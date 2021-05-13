import yfinance as yf
from yfinance import ticker

class stock():
    def __init__(self, ticker = ""):
        self.ticker = ticker
        self.open_price = 0
        self.current_price = 0

    def get_current_price(self):
        ticker = yf.Ticker(self.ticker)
        todays_data = ticker.history(period='1d')
        self.current_price = todays_data['Close'][0]
    
    def get_open_price(self):
        ticker = yf.Ticker(symbol)
        todays_data = ticker.history(period='1d')
        self.open_price = todays_data['Open'][0]
    
    def get_prices(self):
        self.get_open_price()
        self.get_current_price()
