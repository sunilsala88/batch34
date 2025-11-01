# #module/library/package

# import file1

# print(file1.name)
# print(file1.get_stock_info())

# c3=file1.Car('elon',1234,'red')
# print(c3.no_wheel)
# print(c3.car_no)


# import file1 as f1
# print(f1.name)
# import alsjdflkjasldfjlakjsdfkljasdfkajsd as u1
# print(u1.a)

# from file1 import price,get_stock_info
from file1 import *
price=500

print(price)

print(get_stock_info())

c5=Car('abc',589,'green')

from code1.file3 import market_open
print(market_open)