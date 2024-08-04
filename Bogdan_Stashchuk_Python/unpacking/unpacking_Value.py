my_fruits = ['mango', 'kiwi', 'strowberry']

my_mango = my_fruits[0]
my_kiwi = my_fruits[1]
my_strowberry = my_fruits[2]
print(my_strowberry, id(my_strowberry))
print(my_mango)
print(my_kiwi)

mango, kiwi, strowberry = my_fruits


print(strowberry, id(strowberry))
print(mango)
print(kiwi)

list2 = [1, 2, 3]
a, b, c = list2
# a, b, c, d = list2
# ValueError: not enough values to unpack (expected 4, got 3)
print(a)
print(b)
print(c)
print()
print("Tuple")
print()

my_fruits = ('mango', 'kiwi', 'strowberry')
mango, kiwi, strowberry = my_fruits
print(type(my_fruits))
print(strowberry, id(strowberry))
print(mango)
print(kiwi)
