
#list is a datastructure /datatype
d1=[11,22,33,44,'hello',True,5.5]
print(d1)

#indexing and slicing
print(d1[-1])
print(d1[0:3])

#list is mutable
#add elem in a list
d1.append(60)
print(d1)

d1.insert(1,88)
print(d1)

#remove element 
d1.remove(5.5)
print(d1)

d1.pop(2)
print(d1)

#old approach
del d1[1]
print(d1)

d1[1]=99
print(d1)

i=d1.index('hello')
print(i)
