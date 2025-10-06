
#looping/iteration
#type 1
l1=[44,55,66,77,88]
total=0
for i in l1:
    print(i)
    total=total+i
print("Total:", total)

#type 2
print(list(range(100,150)))

#print hello 10 times
for i in range(10):
    print('hello')

#type 3
for i in range(len(l1)):
    print(l1[i])

#generate a list of 50 even num
even_num=[]
for i in range(100):
    if i%2==0:
        even_num.append(i)
print(even_num)


#largest value in the list
list2=[5,6,3,7,4]
max1=list2[0]
for i in list2:
    if i>max1:
        max1=i
print(max1)

#first 10 fib numbers
#1 1 2 3 5 8 13 21 34 55
fib=[1,1]
num1=fib[0]
num2=fib[1]
for i in range(8):
    num3=num1+num2
    fib.append(num3)
    num1=num2
    num2=num3
print(fib)

prices=[4,5,6]
volumes=[1,2,3]

sum_of_pv=0
sum_of_v=0
for i in range(len(prices)):
    sum_of_pv=sum_of_pv+prices[i]*volumes[i]
    sum_of_v=sum_of_v+volumes[i]

vwap=sum_of_pv/sum_of_v
print(vwap)