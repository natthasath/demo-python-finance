import yfinance as yf
import matplotlib.pyplot as plt

class Stock:
    def __init__(self, stock_symbol):
        self.stock = yf.Ticker(stock_symbol)
        self.stock_symbol = stock_symbol

    def get_historical_price_data(self, period="max"):
        return self.stock.history(period=period)

    def get_financials(self):
        return self.stock.financials

    def get_balance_sheet(self):
        return self.stock.balance_sheet

    def get_cashflow(self):
        return self.stock.cashflow

    def plot_historical_data(self):
        historical_data = self.stock.history(period="1y")
        plt.figure(figsize=(10, 6))
        plt.plot(historical_data.index, historical_data['Close'], label=f'{self.stock_symbol} Closing Price')
        plt.title(f'{self.stock_symbol} Historical Closing Price')
        plt.xlabel('Date')
        plt.ylabel('Price (฿)')
        plt.legend()
        plt.grid(True)
        plt.show()