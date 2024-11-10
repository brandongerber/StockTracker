import yfinance as yahooFinance


def getStockValue(symbol, quantity):
    stock = yahooFinance.Ticker(symbol)
    current_price = stock.info['currentPrice']
    return current_price * quantity


def getPortfolioValue(stocks):
    total_value = sum(getStockValue(
        stock['symbol'], stock['quantity']) for stock in stocks)
    return total_value

// change the symbols and quantity to whatever you want 
stocks = [
    {"symbol": "AAPL", "quantity": 3},
    {"symbol": "GOOG", "quantity": 5},
    {"symbol": "TSLA", "quantity": 2},
]

portfolio_value = getPortfolioValue(stocks)

print("Your current Portfolio Status is:")
for stock in stocks:
    stock_value = getStockValue(stock['symbol'], stock['quantity'])
    print(
        f"Amount {stock['quantity']} of Shares {stock['symbol']}, Total value: {stock_value}")

print(f"Total portfolio value: {portfolio_value}")
