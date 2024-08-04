my_range = range(5)
print(my_range)
print(type(my_range))
print(my_range[0])
print(my_range[-1])

print()
for n in my_range:
    print(n)


print()
for n in range(3):
    print(n)

print()
for n in range(2, 5):
    print(n)

print()
for n in range(12, 35, 9):
    print(n)

print()
print(list(range(10, 30, 5)))
print(tuple(range(10, 30, 5)))
print(set(range(10, 30, 5)))

print()
print(dir(my_range))

print()
print(my_range.start)
print(my_range.stop)
print(my_range.step)
print(my_range, 'my_range')
print(my_range.index(3), "index 3")
# print(my_range.index(20), "index 20")
# ValueError: 20 is not in range
print(my_range.count(3))
print(my_range.count(100))
