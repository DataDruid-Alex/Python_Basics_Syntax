# good
# type list tuple dict set

all_nums = [-3, 1, 0, 10, -20, 5]
absolute_nums = []
for num in all_nums:
    absolute_nums.append(abs(num))
print('Absolut: ', absolute_nums)
print('All:', all_nums)

print("-----other_way---------")

all_nums = [-3, 1, 0, 10, -20, 5]
absolute_nums = [abs(num)for num in all_nums]
print('Absolut: ', absolute_nums)
print('All:', all_nums)

print("------Another_example------")
all_nums = [-3, 1, 0, 10, -20, 5]
positive_nums = []
for num in all_nums:
    if num > 0:
        positive_nums.append(num)

print("Positive numbers:", positive_nums)
print('All:', all_nums)

print("-----other_way---------")
all_nums = [-3, 1, 0, 10, -20, 5]
positive_nums = [num for num in all_nums if num > 0]
print("Positive numbers:", positive_nums)
print('All:', all_nums)
