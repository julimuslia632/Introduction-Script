from datetime import datetime, timedelta, timezone
from dateutil import tz

ET = timezone(timedelta(hours=-5))
dt = datetime(2017, 12 ,30 ,15, 9 ,3 , tzinfo = ET)
print(dt)

IST = timezone(timedelta(hours=5, minutes=30))

print(dt.astimezone(IST))
print(dt.replace(tzinfo=timezone.utc))
print(dt.astimezone(timezone.utc))

print("===========================")

et = tz.gettz('America/New_York') # Format: 'Continent/City'       EX:('Europe/London')
last = datetime(2017, 12, 30, 15, 9, 3, tzinfo=et)
print(last)

first = datetime(2017, 10, 1, 15, 23, 25, tzinfo=et)
print(first)


print("=========================")

spring_ahead_159am = datetime(2017, 3, 12, 1, 59, 59)
spring_ahead_159am.isoformat()

spring_ahead_3am = datetime(2017, 3, 12, 3, 0, 0)
spring_ahead_3am.isoformat()
dt1 = (spring_ahead_3am - spring_ahead_159am).total_seconds()
print(dt1)

EST = timezone(timedelta(hours=-5))
EDT = timezone(timedelta(hours=-4))

spring_ahead_159am = spring_ahead_159am.replace(tzinfo = EST)
spring_ahead_159am.isoformat()


spring_ahead_3am = spring_ahead_3am.replace(tzinfo = EDT)
spring_ahead_3am.isoformat()

dt2 = (spring_ahead_3am - spring_ahead_159am).seconds
print(dt2)

print("========================================")
eastern = tz.gettz('US/Eastern')
# 2017-11-05 01:00:00
first_1am = datetime(2017, 11, 5, 1, 0, 0, tzinfo = eastern)
print(tz.datetime_ambiguous(first_1am))

second_1am = datetime(2017, 11, 5, 1, 0, 0, tzinfo = eastern)
second_1am = tz.enfold(second_1am)
dt3 = (first_1am - second_1am).total_seconds()
print(dt3)
first_1am = first_1am.astimezone(tz.UTC)
second_1am = second_1am.astimezone(tz.UTC)
dt3 = (first_1am - second_1am).total_seconds()
print(dt3)