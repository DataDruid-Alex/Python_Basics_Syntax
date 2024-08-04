my_fruits = ["apple", "banana", "lime"]
other_fruits = ["banana", "apple", "lime"]
print(my_fruits == other_fruits)

empty_list = []
print(len(empty_list))
my_fruits = ["apple", "banana", "lime"]
print(len(my_fruits))
posts_ids = [233, 292, 53, 54, 754, 90]
print(len(posts_ids))
user_inputs = [True, "hi", 343, 2.43]
print(len(user_inputs))
print(len("_ _str_ _"), "_ _str_ _")
print(posts_ids, "posts_ids")
print(posts_ids[0], "posts_ids[0]")
print(posts_ids[1], "posts_ids[1]")
print(posts_ids[-1], "posts_ids[-1]")

# change posts_ids
posts_ids[0] = 88
posts_ids[2] = 903342
print(posts_ids, "  changed_posts_ids")
