

stock_prices={'AAPL': 890, 'GOOGL': 2800, 'AMZN': 3400}
porfolio=[]

while True:
    name=input('enter the stock name (type q to quit)')

    if name=='q':
        break
    
    found=stock_prices.get(name)
    if found:
        porfolio.append(name)
    else:
        print('stock name is invalid try again')
print(porfolio)