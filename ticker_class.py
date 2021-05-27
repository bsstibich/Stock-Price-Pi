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
		try:
			ticker = yf.Ticker(self.ticker) #yfinance ticker definition
			todays_data = ticker.history(period='1d') #get today's price history
			self.current_price = todays_data['Close'][0] #get most recent closing price
			return self.current_price
		except:
			self.current_price = 0
			return self.current_price
        
    
	def get_open_price(self):
		try:
			ticker = yf.Ticker(self.ticker) #yfinance ticker definition
			todays_data = ticker.history(period='1d') #get today's price history
			self.open_price = todays_data['Open'][0] #get today's opening price
			return self.open_price
		except:
			self.open_price = 0
			return self.open_price

	def get_prices(self): #update both current and open prices
		self.get_open_price()
		self.get_current_price()
    
	def output(self): #print current prices, will be adapted to LCD soon
		print(self.ticker + ": " + str(self.current_price)) 


		try:
			output_price = str(round(self.current_price,4))
		finally:
			while len(output_price) < 16:
				output_price = " " + output_price
			self.display.lcd_display_string(self.ticker + ':' , 1)
			self.display.lcd_display_string(output_price, 2)


		output_price = str(round(self.current_price,4))
		while len(output_price) < 16:
			output_price = " " + output_price
		self.display.lcd_display_string(self.ticker + ':' , 1)
		self.display.lcd_display_string(output_price, 2)
		


	def lcd_clear(self):
		self.display.lcd_clear()

