my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}
print(my_set)
print(other_set)
print(other_set.intersection(my_set))
print(other_set.intersection('abc'), "   ('abc')    ")
print(other_set.intersection(['a', 'b', 'c']), "  ['a','b','c']   ")

print()

print(my_set.union(other_set))
print(other_set.issubset(my_set))

print(my_set.difference(other_set))
print(my_set-other_set)

print()
d = my_set.discard('d')
d2 = my_set.discard('dfsdfs')
# r = my_set.remove('dfls')
r = my_set.remove('y')
print(my_set, d, d2, r)

print()
my_set = {'abc', 'd', 'f', 'y'}
copied_set = my_set.copy()
print(my_set)
print(copied_set)
my_set.add('-_-')
copied_set.add(':)')
print("my_set", my_set)
print("copied_set", copied_set)
print()
print(my_set & copied_set)

print()
print(my_set.symmetric_difference(copied_set))
print((my_set | copied_set)-(copied_set & my_set))
