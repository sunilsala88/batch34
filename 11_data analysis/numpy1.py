

l1=[22,33,44,55,6.6]
print(l1)

print(l1+l1)
print(l1*3)

#pip install numpy
import numpy as np
np1=np.array(l1)
print(np1+np1)
print(np1*3)

print(list(range(10)))
print(np.arange(10))

m1=[[11,12,13], [14,15,16], [17,18,19]]
print(m1)
mp1=np.array(m1)
print(mp1)
print(mp1[1,1])

a1=np.arange(25).reshape(5,5)
print(a1)
print(a1[4,3])

a2=np.random.randint(100,200,16).reshape(4,4)
print(a2)

import pandas as pd
df1=pd.DataFrame(a1)
print(df1)

df2=pd.DataFrame(a2)
print(df2)