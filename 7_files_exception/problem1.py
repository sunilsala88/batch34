

f1=open('file1.txt','r')
d=f1.read()
f1.close()

f2=open('file2.txt','w')
f2.write(d)
f2.close()
