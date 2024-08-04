c = 99


def my_fn(a, b):
    print(c, '     _5_ :)')
    print(a, b)
    d = 10
    print()
    print("This is show local(my_fn) access variable(fun) and method:")
    print(dir())
    print()


c = 5
my_fn('abc', 'xyz')
c = 13
# print(a)
# NameError: name 'a' is not defined

print()
print("This is show global access variable(fun) and method:")
print()
print(dir())
