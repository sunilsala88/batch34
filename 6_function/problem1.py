

stock_prices={'AAPL': 890, 'GOOGL': 2800, 'AMZN': 3400,'NVDA':789}



def take_input(stock_prices):
    porfolio={}

    while True:
        name=input('enter the stock name (type q to quit)')

        if name.lower()=='q':
            break
        if name=='NVDA':
            print('this stock is not tradeble try some thing else')
            continue
        
        found=stock_prices.get(name)
        if found:
            porfolio.update({name:found})
        else:
            print('stock name is invalid try again')

    return (porfolio)

p=take_input(stock_prices)
print(p)