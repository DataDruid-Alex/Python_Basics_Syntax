from datetime import datetime
from datetime import time
from datetime import date

# date
print(type(date))
my_date = date(2004, 6, 20)
print(my_date)
print(my_date.day)
print(my_date.month)
print(my_date.year)
print(my_date.isocalendar())
print()
# time
my_time = time(21, 13, 32, 100)
print(my_time)
print(my_time.hour)
print(my_time.minute)
print(my_time.second)
print(my_time.microsecond)
print()

my_datetime = datetime(2004, 6, 20, 15, 23, 14, 295)
print(my_datetime)
print(my_datetime.isoformat())
print()
print(my_datetime.now())
a = datetime(2000, 2, 20, 17)
print(a.now())
