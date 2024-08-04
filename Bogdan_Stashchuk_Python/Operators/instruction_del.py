my_dict = {
    'a': True,
    'b': 8,
}
print(my_dict)
del my_dict['a']
print(my_dict)
my_dict.__delitem__('b')
print(my_dict)


# print(del my_dict['a'])
# SyntaxError: invalid syntax
# print(return my_dict['a'])
# SyntaxError: invalid syntax
print()
my_list = [2, 4]
print(my_list)
del my_list[0]
print(my_list)
my_list.__delitem__(0)
# del my_list.__delitem__(0)
# SyntaxError: cannot delete function call
print(my_list)
