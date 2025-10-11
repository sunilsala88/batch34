

#type 4
stock_prices={'AAPL': 890, 'GOOGL': 2800, 'AMZN': 3400}

# for stock in stock_prices:
#     print(stock)
#     print(stock_prices[stock])

print(list(stock_prices.keys()))
print(list(stock_prices.values()))
print(list(stock_prices.items()))

for i,j in stock_prices.items():
    print(i,j)
    