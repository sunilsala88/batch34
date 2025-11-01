name='tsla'
price=200

def get_stock_info():
    return f'stock name is {name} and price is {price}'

class Car:
    no_wheel=4
    def __init__(self,owner1,car_no,color):
        self.owner=owner1
        self.car_no=car_no
        self.color=color
    
    def get_info(self):
        return f'car owner is {self.owner} and car no is {self.car_no}'