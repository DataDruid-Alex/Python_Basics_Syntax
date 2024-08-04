def my_fn():
    global a
    a = 15
    global d
    d = 'dfdkf'
    # c = globals()
    # print(c)
    # 'a': 15, 'd': 'dfdkf'}


my_fn()
print(a)

print()
print('_____NEW func____')
a = 10


def fn():
    global a
    a = 99


fn()
print(a)
