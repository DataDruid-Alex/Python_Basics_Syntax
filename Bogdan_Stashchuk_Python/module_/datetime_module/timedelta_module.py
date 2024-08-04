from datetime import datetime, timedelta
print(timedelta)
print()

my_datetime = datetime(2004, 6, 20)
print(my_datetime)
print(my_datetime+timedelta(days=10000, minutes=15, hours=20, seconds=30))
print(my_datetime-timedelta(days=10000, minutes=15, hours=20, seconds=30))


print(id(my_datetime))
print(id(my_datetime+timedelta(days=10000, minutes=15, hours=20, seconds=30)))
print(id(my_datetime-timedelta(days=10000, minutes=15, hours=20, seconds=30)))
