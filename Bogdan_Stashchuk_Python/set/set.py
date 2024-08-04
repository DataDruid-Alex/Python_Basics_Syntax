my_fruits = {'apple', 'banana', 'apple', 'strowberry'}
print(my_fruits)
post_ids_list = [1, 2, 1, 1, 1, 1, 94, 31, 1, 2, 3]
print(len(post_ids_list))
print(post_ids_list)
print("set")
post_ids = set(post_ids_list)
print(post_ids, type(post_ids))
print(len(post_ids), 'len')
user_inputs = {"dsfds", True, 3443, 'sd', (3, 2, 4)}
print(user_inputs)

print()
my_fruits = {'apple', 'banana', 'apple', 'strowberry'}
other_fruits = {'strowberry', 'apple', 'banana'}
print(my_fruits == other_fruits, "my_fruits==other_fruits?")

# print(my_fruits[1])
# TypeError: 'set' object is not subscriptable
