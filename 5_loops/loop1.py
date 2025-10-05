
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