import yfinance as yahooFinance


def getStockValue(symbol, quantity):
    try:
        stock = yahooFinance.Ticker(symbol)
        current_price = stock.info.get('currentPrice')
        if current_price is not None:
            return current_price * quantity
        else:
            print(f"Error: Could not retrieve price for {symbol}.")
            return 0
    except Exception as e:
        print(f"Exception occurred for {symbol}: {e}")
        return 0


def getPortfolioValue(stocks):
    total_value = sum(getStockValue(stock['symbol'], stock['quantity']) for stock in stocks)
    return total_value


stocks = [
    {"symbol": "GOGL", "quantity": 3},
    {"symbol": "MDT", "quantity": 2},
    {"symbol": "PLTR", "quantity": 5},
    {"symbol": "ZETA", "quantity": 8},
    {"symbol": "TTOO", "quantity": 5},
    {"symbol": "ATCH", "quantity": 14},
]

portfolio_value = getPortfolioValue(stocks)

print("Portfolio Status:")
for stock in stocks:
    stock_value = getStockValue(stock['symbol'], stock['quantity'])
    print(
        f"Holding {stock['quantity']} shares of {stock['symbol']}, Total value: {stock_value}")

print(f"Total portfolio value: {portfolio_value}")
