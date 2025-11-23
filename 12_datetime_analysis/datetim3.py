
import pandas as pd

df=pd.read_csv('/Users/algo trading 2025/batch34/12_datetime_analysis/sbin.csv')

print(df)

df['date']=pd.to_datetime(df['date'])
df=df.set_index('date')
print(df)
print(df.info())