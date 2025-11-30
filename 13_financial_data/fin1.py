
#equity
#future
#option
#forex
#crypto
#bond

#tick price
#candle chart
#high,low,open,close
#yahoo finance
#yfinance
#broker

import yfinance as yf
# data=yf.download(['GOOG'],period='1y',multi_level_index=False)
# print(data)

# data=yf.download(['GOOG'],start='2021-01-01',end='2021-12-31',multi_level_index=False)
# print(data)

# data=yf.download(['^NSEI'],period='5d',multi_level_index=False,interval='1m',ignore_tz=True)
# print(data)


# data=yf.download(['EURUSD=X'],period='100d',multi_level_index=False,interval='1h',ignore_tz=True)
# print(data)

import datetime as dt
data=yf.download(['GOOG'],start=dt.datetime(2021,1,1),end=dt.datetime(2021,12,31),multi_level_index=False)
print(data)