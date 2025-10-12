

l1=[33,44,55,66,77,88]

count=0
for i in l1:
    if i%2!=0:
        count=count+1

print(count)

i=0
count=0
while True:
    if i==len(l1):
        break
    
    if l1[i]%2!=0:
        count=count+1

    i=i+1
print(count)



for i in range(51):
    if i%3==0 or i%5==0:
        print(i,end=' ')

print('')
i=0
while True:
    if i>50:
        break
    if i%3==0 or i%5==0:
        print(i,end=' ')
    i=i+1

print(' ')
sent='Python is fun to learn'
count=0
for i in sent:
    if i==' ':
        count=count+1
count=count+1
print(count)