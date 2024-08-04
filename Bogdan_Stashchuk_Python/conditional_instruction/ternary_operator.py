statement1 = True
statement2 = False
print(statement1 if 4 == 0 else statement2)
print(statement1 if 4 > 0 else statement2)
stat1 = 'First'
stat2 = 'Second '
print(stat1 if 4 == 0 else stat2)
print(stat1 if 4 > 0 else stat2)


my_number = 7.9
print('is int' if isinstance(my_number, int)else "is not int")

if isinstance(my_number, int):
    print('is int')
else:
    print('is not int')

product_qnt = 99
print('in stock') if product_qnt > 0 else print('out of stock')

temp = +10
# print('hot') if temp > 19 else print("cold")
whether = "hot" if temp > 19 else "cold"
print(whether)
