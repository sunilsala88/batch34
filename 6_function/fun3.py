#local and global variable




def average(numbers:list)->int:
    #doc string
    """this funtion will return average value"""

    total=0
    print(price)
    for i in numbers:
        total=total+i
    avg=total/len(numbers)
    return avg


price=100
a=average([1,2,3])
print(a)

print(price)


#local var->var created inside the funtion
#local var cannot be accessed outside the function
#global var can be accessed anywhere in the code
#but it should exist before using
#if you want to edit global var then you have to use global keyword
