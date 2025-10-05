
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