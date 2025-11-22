
import datetime as dt

n1=dt.datetime(2025,11,22,11,30,15)
print(n1)
current=dt.datetime.now()
print(current)

def strategy():
    print('running')


start_time=dt.datetime(2025,11,22,17,13,15)
end_time=dt.datetime(2025,11,22,17,20,55)
import time
while start_time<dt.datetime.now()<end_time:
    ct=dt.datetime.now()
    if ct.second==1:
        strategy()
    print(ct)
    time.sleep(1)