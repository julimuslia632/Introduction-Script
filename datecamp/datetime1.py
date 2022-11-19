from datetime import datetime
dt = datetime(2017, 10 ,1 ,15, 23 , 25) # as 2017-10-1 3:23:25
print(dt)
dt_hr = dt.replace(minute=0, second=0)
print(dt_hr)
print(dt.strftime("%Y-%m-%d %H:%M:%S hi"))
dt1 = datetime.strptime("12/30/2017 15:19:13",
                      "%m/%d/%Y %H:%M:%S")
print(dt1)
ts = 1514464153.0
print(datetime.fromtimestamp(ts))


start = datetime(2017, 10 ,8, 23, 45 ,34)
end = datetime(2017, 10 ,9, 14, 14, 14)

duration = end -start 
print(duration.total_seconds())