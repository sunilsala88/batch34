


prices=[200,300,400,600,700]

#function defination
def average(numbers:list) ->float:
    if type(numbers)!=list:
        return 0

    total=0
    for i in numbers:
        total=total+i
    avg=total/len(numbers)
    return (avg)

customers=[3,4,6,7,1]

#function call
a=average(prices)
print(a)

#function call
b=average(customers)
print(b)

c=average(44)
print(c)


ans=get_fib(10)
[1,1,3,]