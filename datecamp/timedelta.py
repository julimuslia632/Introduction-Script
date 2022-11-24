from datetime import timedelta
from datetime import date
from datetime import datetime

td = timedelta(days=29)
d1 = date(2017, 1 ,1)
print(d1 + td)

start = datetime(2017, 10 ,8, 23, 45 ,34)
end = datetime(2017, 10 ,9, 14, 14, 14)

duration = end -start 
print(duration.total_seconds())

delta1 = timedelta(seconds=1)
delta2 = timedelta(days=1, seconds=1)
delta3 = timedelta(weeks=-1)
print(duration.total_seconds())