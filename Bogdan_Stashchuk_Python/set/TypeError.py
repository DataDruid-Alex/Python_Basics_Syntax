posts_ids = {10, 25, 15, 28}
posts_ids_list = [10, 25, 15, 28]

n = 3
p_get = posts_ids_list.__getitem__(n)
p = posts_ids_list[n]
print(p_get, p)

a = 10
# a[0]
# TypeError: 'int' object is not subscriptable
print(dir(a))
