

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