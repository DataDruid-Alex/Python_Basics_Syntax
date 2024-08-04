user_data = ['Oleksandr', 20]


def user_info(name, coments_qnt):
    if not coments_qnt:
        return f"{name} has no comments"
    return f"{name} has {coments_qnt} comments"


print(user_info(*user_data))
# print(user_info(user_data))
# TypeError: user_info() missing 1 required
# positional argument: 'coments_qnt'
print()
print(user_info(user_data[0], user_data[1]))
# print(user_info(user_data, 2))
# ['Oleksandr', 20] has 2 comments

# user_data = ['Oleksandr', 20, True]
# print(user_info(*user_data))
# TypeError: user_info() takes 2 positional arguments but 3 were given

# print(user_info(**user_data))
# TypeError: __main__.user_info() argument after **
# must be a mapping, not list

print("________________")
my_name, qnt_com = user_data
print(user_info(my_name, qnt_com))
