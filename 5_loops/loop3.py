

number=0
while True:
    if number==100:
        break
    if number%2==0:
        print(number)
    number=number+1

fib=[1,1]
num1=fib[0]
num2=fib[1]
count=0
while True:
    if count==8:
        break
    num3=num1+num2
    fib.append(num3)
    num1=num2
    num2=num3
    count=count+1
print(fib)


list1=[44,55,66,77]
index1=-1
new_list=[]
while True:
    if index1==-(len(list1)+1):
        break
    new_list.append(list1[index1])
    index1=index1-1
print(new_list)

str1='tsla'
ans=''
index1=-1

while True:
    if index1==-(len(list1)+1):
        break
    ans=ans+str1[index1]
    index1=index1-1

print(ans)