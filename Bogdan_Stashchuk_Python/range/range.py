my_range = range(7)
print(my_range, type(my_range))
print(list(my_range))
print(tuple(my_range))
print(set(my_range))

print()

rang = range(10, 20, 3)
print(type(rang), rang)
print(list(rang))
print(rang[0])
print(rang[1])
print(rang[2])
print(rang[3])
# print(rang[4])
# IndexError: range object index out of range

print()
print("range in for")

for n in range(10, 20, 3):
    print(n)
