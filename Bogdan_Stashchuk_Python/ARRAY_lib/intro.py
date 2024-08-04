from array import array
my_int_array = array('i', [1, 2, 3, 4, 5, 6, 11, 22, 33, 44, 0, -11, 1])

with open("my_array.bin", 'wb')as my_file:
    my_int_array.tofile(my_file)
imported_array = array('i')
with open("my_array.bin", 'rb') as my_file:
    imported_array.fromfile(my_file, 3)
    print(my_int_array)
    print(imported_array)
imported_array.reverse()
print(imported_array)
# print(my_int_array)
# print(type(my_int_array))
# my_int_array.append(999)
# print(my_int_array)
# print(my_int_array.count(1))
# my_int_array.pop()
# print(my_int_array)
# for elem in my_int_array:
#     print(elem)
# print(my_int_array[0])
