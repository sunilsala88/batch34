
import datetime as dt

ct=dt.datetime.now()
print(ct)

#date
#time
#datetime
#timedelta



a='2025-11-30'
print(a)
d1=dt.date(2025,11,30)
print(d1)
print(d1+dt.timedelta(days=1))

dt1=dt.datetime(2025,11,30,11,11,11)
print(dt1)
print(dt1+dt.timedelta(minutes=2))