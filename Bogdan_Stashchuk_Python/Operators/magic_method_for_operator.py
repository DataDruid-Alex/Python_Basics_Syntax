a = [1, 2]
b = [1, 2]

print(a == b)
print(a.__eq__(b))

print()
print(a.__eq__)
print()
print(a is b, '  a is b')
print(id(a) == id(b), '   id(a)==ida(b)')
print(id(a).__eq__(id(b)), "   id(a).__eq__(id(b)")
print()
print(id(a))
print(hex(id(a)))
