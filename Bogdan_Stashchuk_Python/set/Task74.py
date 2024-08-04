my_set = {1, 2, 4, 3, 5, 6, 7}
print(my_set, type(my_set))
my_set.add(8)
print(my_set)
other_set = {1, 5, 6, 12}
new_set = my_set & other_set
print()
print(other_set)
print(new_set)
print()
my_list = list(new_set)
print(my_list, type(my_list))

my_set.difference_update(other_set)
print(my_set)
