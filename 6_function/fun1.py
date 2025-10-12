


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

def get_fib(num:int)->list:

    fib=[1,1]
    num1=fib[0]
    num2=fib[1]
    for i in range(num-2):
        num3=num1+num2
        fib.append(num3)
        num1=num2
        num2=num3
    return fib

ans=get_fib(10)
print(ans)

def reverse_list(list1:list)->list:

    index1=-1
    rev=[]
    while True:
        rev.append(list1[index1])
        index1=index1-1

        if index1<-len(list1):
            break
    return rev

l2=reverse_list([1,2,3])
print(l2)


l1=[33,44,55]
#-1,-2,-3

i=-1
while True:
        
    print(i)
    i=i-1
    if i==-4:
        break


print(l1[-3])