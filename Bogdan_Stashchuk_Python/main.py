# list=[1,2,3]
print(list)
dict1 = {'min': 1, 'max': 12}
print(dict1)


def my_fn(a, b):
    a = a+b
    c = a*b
    return c


print('Result =', my_fn(3, 6))
print(type(my_fn))
print(id(my_fn))
print(len('adsca'))
# print(sum('90.4'+'45'))

name = input("Enter your name: ")
print(name)

print(print())
print(print)

# name=input("Enter your name: ")
# print(name)


def my_fun(a, b):
    a = a+4
    c = a+b*(a-8)
    return c


print(my_fun(3, 7))
