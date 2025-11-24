# import datetime as dt
# import pytz
# tz1=pytz.timezone('Asia/Kolkata')
# tz2=pytz.timezone('US/Eastern')
# t1=dt.datetime.now(tz=tz2)
# print(t1)

import pendulum as dt
p1=dt.now(tz='Asia/Kolkata')
print(p1)

