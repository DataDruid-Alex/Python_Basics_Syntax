my_disk = {}
print(id(my_disk))
print(type(my_disk))
my_disk['brand'] = 'Samsung'
my_disk['price'] = 10_000
print(my_disk)
print()
print(my_disk.popitem())
print(my_disk, "  my_disk")
print(my_disk.get('type', 'hdd'))
print()

new_disk = my_disk.copy()
new_disk['type'] = 'SSD'
print(my_disk, 'my_disk')
print(new_disk, 'new_disk')
print(id(my_disk) == id(new_disk))
print("id_MY=", id(my_disk), "id_New=", id(new_disk))

print()

print(len(new_disk))
