from decouple import config
from finance.finance import Stock

if __name__ == "__main__":
    # Get user input for stock symbol
    stock_symbol = input("Enter stock symbol: ")

    # Create an instance of StockData
    stock_data = Stock(stock_symbol)

    # Get historical price data
    historical_data = stock_data.get_historical_price_data()
    print("Historical Price Data:")
    print(historical_data.head())

    # Get financials
    financial_data = stock_data.get_financials()
    print("\nFinancials:")
    print(financial_data)

    # Get balance sheet
    balance_sheet = stock_data.get_balance_sheet()
    print("\nBalance Sheet:")
    print(balance_sheet)

    # Get cash flow
    cashflow_data = stock_data.get_cashflow()
    print("\nCash Flow:")
    print(cashflow_data)

    stock_data.plot_historical_data()