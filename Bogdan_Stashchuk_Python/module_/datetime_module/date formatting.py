from datetime import datetime
my_datetime = datetime(2004, 6, 20, 17, 25)
print(my_datetime)

print(my_datetime.strftime('%d/%m/%Y'))
print(my_datetime.strftime('%d/%m/%Y-%H:%M:%S'))


# print(my_datetime.strftime('%d-%b-%Y'))
# print(id(my_datetime))

date_str = '2008:02:17'
converted_date = datetime.strptime(date_str, '%Y:%m:%d')
print(date_str)
print(converted_date)
