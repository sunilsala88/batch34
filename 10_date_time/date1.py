
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

current=dt.datetime(2024,1,1)

print(current.month)

while True:
    if current.year==2025:
        break    
    day1=dt.timedelta(days=1)
    current=current+day1
    print(current)

    