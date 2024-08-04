def fn(a, b):
    print(id(a), 'id a')
    a = a + 1
    print(id(a), 'id a change')
    c = a+b
    return c


num_one = 10
num_two = 5

print(id(num_one), 'num_one')
res = fn(num_one, num_two)
print(id(num_one), 'num_one')
print(res)
print(num_one)  # num_one not change
