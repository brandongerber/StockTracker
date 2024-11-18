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

def getUserInput():
    stocks = []
    while True:
        symbol = input("Enter stock symbol (or type 'done' to finish): ")
        if symbol.lower() == 'done':
            break
        try:
            quantity = int(input(f"Enter quantity of shares for {symbol}: "))
            stocks.append({"symbol": symbol, "quantity": quantity})
        except ValueError:
            print("Invalid quantity. Please enter an integer value for quantity.")
    
    return stocks

stocks = getUserInput()
portfolio_value = getPortfolioValue(stocks)

print("\nPortfolio Status:")
for stock in stocks:
    stock_value = getStockValue(stock['symbol'], stock['quantity'])
    print(f"Holding {stock['quantity']} shares of {stock['symbol']}, Total value: {stock_value:.2f}")

print(f"\nTotal portfolio value: {portfolio_value:.2f}")
