
import datetime as dt

n1=dt.datetime(2025,11,22,11,30,15)
print(n1)
current=dt.datetime.now()
print(current.time())
print(current.weekday())
print(current.date())
print(current.minute)

# def strategy():
#     print('running')


# start_time=dt.datetime(2025,11,22,17,13,15)
# end_time=dt.datetime(2025,11,22,17,20,55)
# import time
# while start_time<dt.datetime.now()<end_time:
#     ct=dt.datetime.now()
#     if ct.second==1:
#         strategy()
#     print(ct)
#     time.sleep(1)



#epoch to datetime
n1=1763812758
d1=dt.datetime.fromtimestamp(n1)
print(d1)


#datetime to epoch
print(current.timestamp())

#str to datetime
s1='2025-01-01'
f='%Y-%d-%m'
ds1=dt.datetime.strptime(s1,f)
print(ds1)



#datetime to str
s3=current.strftime('%Y-%m')
print(s3)