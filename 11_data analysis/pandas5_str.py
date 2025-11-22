

s1='hello'
print(s1.upper())
print(s1.replace('h','a'))

import pandas as pd
df=pd.read_csv('/Users/algo trading 2025/batch34/11_data analysis/sp500.csv')
print(df)

print(df['Name'])
#easy

#accessor
print(df['Name'].str.replace(' ','-'))

#diff
temp_list=[]
for i in df['Name']:
    temp_list.append(i.replace(' ','-'))
df['Name']=temp_list
print(df)

df1=pd.read_csv('/Users/algo trading 2025/batch34/11_data analysis/unicorn.csv')
print(df1)

l1=[]
for i in df1['Funding']:
    d=str(i)
    l1.append(d)

df1['new']=l1
print(df1)

df1['Valuation']=df1['Valuation'].astype('str')
print(df1.info())
