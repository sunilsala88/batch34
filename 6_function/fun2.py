

#parameter / argument
#fun defination
def average(numbers:list)->int:
    #doc string
    """this funtion will return average value"""
    total=0
    for i in numbers:
        total=total+i
    avg=total/len(numbers)
    return avg

a=average([1,2,3,4,5])
print(a)


def multiply(num1,num2):
    ans=num1*num2
    return ans

def division(num1,num2=1):
    ans=num1/num2
    return ans

#positional argument
a=division(3,2)
print(a)

#keyword argument
b=division(num2=3,num1=2)
print(b)

#default argument
c=division(10)
print(c)