for el in [4, 2, 9, 'ei8', False, '9uis', 9.7]:
    print(type(el), el)

print(el)
print(dir())

print("------------")
for key in {'id': 899, 'is_log': True}:
    print(type(key), key, )

my_dict = {'id': 899, 'is_log': True}
print("------------")
for key in my_dict:
    print(type(key), key, ":", my_dict[key])
