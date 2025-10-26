#class
#is the blueprint of object
#object
#is the instance of a class


#attribute
#any var that you create inside a class is call attribute
#class attribute


#instance\object attribute

class Car:
    no_wheel=4
    windows=True

    def __init__(self,owner,car_no,color):
        self.owner=owner
        self.car_no=car_no
        self.color=color

c1=Car('sam',568,'red')
print(c1.no_wheel)
print(c1.car_no)

c2=Car('matt',678,'black')
print(c2.no_wheel)
print(c2.car_no)