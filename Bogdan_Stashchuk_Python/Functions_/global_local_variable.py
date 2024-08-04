a = 10


def my_fn():
   # print(a)
   # UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
    a = True
    b = 15
    print(a, 'a')
    print(b, 'b')


my_fn()
print(a, 'a_external')
# print(b)
# NameError: name 'b' is not defined
