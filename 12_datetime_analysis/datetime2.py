
import pandas as pd
import datetime as dt
df=pd.read_csv('/Users/algo trading 2025/batch34/11_data analysis/unicorn.csv')
print(df)
print(df.info())
# df['Date Joined']=pd.to_datetime(df['Date Joined'],format='%d-%m-%Y')

l1=[]
for i in df['Date Joined']:
    l1.append(dt.datetime.strptime(i,'%d-%m-%Y'))

df['Date Joined']=l1

print(df.info())
print(df)

#diff imp
l1=[]
for i in df['Date Joined']:
    l1.append(i.year)
df['year']=l1
print(df)

df['month']=df['Date Joined'].dt.month
print(df)