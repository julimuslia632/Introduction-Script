from datetime import date
d = date(2017, 11 , 5)
# ISO format: YYYY-MM-DD
print(d) 
print([d.isoformat()])
some_dates = ["2001-01-01" , "1999-12-31"]
print(sorted(some_dates)) # still sorted even if it is string

print(d.strftime("%Y"))  # it only prints years
print(d.strftime("%m"))  # it gives us the months
print(d.strftime("%d"))  # it gives us the days 
print(d.strftime("%Y/%m/%d")) # we changet it in our way
