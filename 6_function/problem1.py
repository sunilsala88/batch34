

stock_prices={'AAPL': 890, 'GOOGL': 2800, 'AMZN': 3400,'NVDA':789}

def display(stock_prices):
    for i,j in  stock_prices.items():
        print(i,":",j)

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

display(stock_prices)
p=take_input(stock_prices)
print(p)

def maximum(a,b):
    if a>b:
        return a
    else :
        return b