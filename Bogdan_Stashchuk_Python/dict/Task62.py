my_dict = {}
key1 = input("Enter name key1: ")
value1 = input("Enter value key1 ")

key2 = input("Enter name key2: ")
value2 = input("Enter value key2 ")

key3 = input("Enter name key3: ")
value3 = input("Enter value key3 ")
my_dict[key1] = value1
my_dict[key2] = value2
my_dict[key3] = value3

my_dict['job'] = 'Financial manager'
print(my_dict)
print()
del my_dict[key2]  # ????????????????????????
print(my_dict)
