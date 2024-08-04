my_list = []
my_dict = {}
full_list = [1, 3, 'sdf', True, False, 3.2]
other_full_list = [99, 'reoo', 4j, 34]
print(not my_list)
print(not full_list)
print(not not my_list)
print(not not full_list)
print(other_full_list or full_list)
print(len(other_full_list) < 0 or full_list)
print(len(other_full_list) > 0 or full_list)
print()
print(full_list and my_dict)
print(bool(full_list and my_dict))
print()
full_list and print("_full_list__List is not empty")
my_list and print("__my_list_List is not empty")
# print("List is empty") or my_list
print()
my_list or print("__my_list_List___List is empty")
full_list or print("__full_list____List is empty")
