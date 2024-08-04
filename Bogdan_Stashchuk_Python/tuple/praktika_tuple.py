my_nums = (10, 5, 100, 0, 5, 5)
print(type(my_nums))

# del my_nums[1]
# TypeError: 'tuple' object doesn't support item deletion
print(my_nums.count(5))
index_one = my_nums.index(5)
index_two = my_nums.index(5, index_one+1)  # ! +1
index_three = my_nums.index(5, index_two+1)  # ! +1
print(index_three)

print()

my_list = list(my_nums)
print(my_list)
my_list.append(7)
print(my_list)
my_nums = tuple(my_list)
print(my_nums)
