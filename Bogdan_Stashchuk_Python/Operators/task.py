a = {1, 3, 2, 4, 5, 1, 1, 2, 4, 5}
b = {1, 5, 4, 2, 3}
print(type(a), a)
print(type(b), b)
print(a == b)
print(a is b, "     False because set is mutable object")
print(a in b)
print()
a_tuple = tuple(a)

print('1' in a, "'1' in a")
print(1 in a, "1 in a")
print()

for i in range(5):
    print(a_tuple[i] in b, i, 'in a', a_tuple[i])
print()
print(dir(a))
