#class
#is the blueprint of object
#object
#is the instance of a class


#attribute
#any var that you create inside a class is call attribute
#class attribute


#instance\object attribute

#method
#any function inside a class is called method


#__init__ method is called contructor:
#constructor is the first function which is executed when you create an object
class Car:
    no_wheel=4
    windows=True

    def __init__(self,owner1,car_no,color):
        self.owner=owner1
        self.car_no=car_no
        self.color=color
    
    def get_info(self):
        return f'car owner is {self.owner} and car no is {self.car_no}'

c1=Car('sam',568,'red')
print(c1.no_wheel)
print(c1.car_no)
print(c1.get_info())
c2=Car('matt',678,'black')
print(c2.no_wheel)
print(c2.car_no)
print(c2.get_info())


#create a class called circle
#1 class attribute called pi
#1 instance attribute called radius
#2 methods
#area() #pi*r*r
#circumference() 2*pi*r

class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius

    def __repr__(self):
        return str(self.radius)
    
    def area(self):
        return self.pi*self.radius*self.radius

    def circumference(self):
        return 2*self.pi*self.radius

c1=Circle(10)
c2=Circle(20)

print(c1.area())
print(Circle.area(c1))
print(c2.area())

print(c1)
print(c2)

# class Bank:
#     bank_name='jp morgan'

#     def __init__(self,name,acc_no,money):
#         self.name=name
#         self.acc_no=acc_no
#         self.balance=money
    
#     def __repr__(self):
#         return self.name
    
#     def withdraw(self,amount):
#         if amount<self.balance:
#             self.balance=self.balance-amount
            
#         else:
#             print('not enough money')
#         return self.balance

#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         return self.balance


# u1=Bank('sanjay',98,1000)
# print(u1.name)
# print(u1.deposit(5000))
# print(u1.withdraw(2000))
# print(u1)

#all methods inside class should have self
#to access any attribute you have to use self