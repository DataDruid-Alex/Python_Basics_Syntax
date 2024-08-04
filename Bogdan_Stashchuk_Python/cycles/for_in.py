my_list = [89, "Type", 999.094, True, (4, 2), 'uno']
for elem in my_list:
    print(elem)

print("-----------")
my_tuple = (True, '1920x1080', 56)
for elem in my_tuple:
    print(elem)


print("-----------")
my_dict = {
    'z': "Barthon",
    'x': 888,
    'y': True,
}
for key in my_dict:
    print(key, my_dict[key])
