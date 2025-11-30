
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
data=yf.download('GOOG',period='max',multi_level_index=False)
print(data)