# immutable object
my_number = 10
other_number = 10
print(id(my_number), 'my_num')
print(id(other_number), 'other_num')
print(id(10), '10')
other_number = 4
print(id(other_number), 'change other_num')


print()
first_num = 10
second_num = first_num
print(id(first_num), 'first', first_num)
print(id(second_num), 'second', second_num)
second_num += 5
print(id(first_num), 'first', first_num)
print(id(second_num), 'second', second_num)
