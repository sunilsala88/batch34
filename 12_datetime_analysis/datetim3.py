
import pandas as pd

df=pd.read_csv('/Users/algo trading 2025/batch34/12_datetime_analysis/sbin.csv')

print(df)

df['date']=pd.to_datetime(df['date'])


tz1='Asia/Kolkata'
tz2='US/Eastern'
#add a time zone
df['date']=df['date'].dt.tz_localize(tz=tz1)
print(df)
#remove a timezone
# df['date']=df['date'].dt.tz_localize(tz=None)

#convert timezone
df['date']=df['date'].dt.tz_convert(tz=tz2)

df=df.set_index('date')
print(df)
print(df.info())