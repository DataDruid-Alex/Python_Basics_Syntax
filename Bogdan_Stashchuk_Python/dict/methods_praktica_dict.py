my_disk = {}
print(id(my_disk))
print(type(my_disk))
my_disk['brand'] = 'Samsung'
my_disk['price'] = 10_000
print(my_disk)
print(id(my_disk))
print()
print(my_disk.items())
print(type(my_disk.items()))
print()
print(my_disk.keys())
print(type(my_disk.keys()))

print()
print("This is list keys dict")

my_list = list(my_disk.keys())
print(my_list)
