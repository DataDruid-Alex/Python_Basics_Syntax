def sum_nums(*args):
    print(args)
    print(type(args))
    print(args[0])
    return sum(args)


print(sum_nums(2, 3, 7))
# print(sum(2, 3, 7))
# TypeError: sum() takes at most 2 arguments (3 given)
print(sum((2, 3, 7)))  # ??????????????????

print()


def get_posts_info(name, posts_qnty):
    info = f"{name} wrote {posts_qnty} posts"
    return info


info = get_posts_info('Oleksandr', 100)
print(info)
