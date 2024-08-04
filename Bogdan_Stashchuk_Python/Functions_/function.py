a = 2
b = 4
c = a+b
print(c)

a = 99
b = 11
c = a+b
print(c)

q = 2
w = 4
e = q+w
print(e)

print()


def sum(a, b):
    sum = a+b
    print(sum)  # :-_-
   # return (sum)


sum(2, 4)
sum(99, 11)
sum(2, 4)
print(type(sum))
print(dir(sum))

print()
a = sum(100, 120)
print()
print(a)


def my_fn(a, b):
    a += 1
    c = a+b
    print(c)
    return c


print()
res = my_fn(10, 3)
