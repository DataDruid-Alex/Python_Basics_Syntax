my_fruit = 'lime'
other_fruit = 'apple'
new_fruit = 'strowberry'
all_fruits = (my_fruit, other_fruit, new_fruit)
print(all_fruits)
post_ids = (145, 321, 134, 532, 234, 241)
# print(post_ids[100])
# IndexError: tuple index out of range

n = 1
if len(post_ids) > n:
    print(post_ids[n])
else:
    print("Index not the available range")

print("my possible change get() in tuple")
