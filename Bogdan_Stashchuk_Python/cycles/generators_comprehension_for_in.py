from sys import getsizeof
nums = (3, 5, 10)
squares = (num*num for num in nums)
print(squares, type(squares))
# -_-      _-_       -_-
print()
print("------Another example---------")
print()

squares = (num*num for num in range(6))
print(squares)
print(type(squares))
for num in squares:
    print(num)
print()
print("------list---------")
print()

nums = (3, 5, 10)
gen = (num*num for num in nums)
squares = list(gen)
print(squares, type(squares))

print()
print("------tuple---------")
print()

nums = (3, 5, 10)
gen = (num*num for num in nums)
squares = tuple(gen)
print(squares, type(squares))

print()
print("------Advantage generator---------")
print()

squares_gen = (num*num for num in range(100_000_000))
print(getsizeof(squares_gen))
print(type(squares_gen))

for elem in squares_gen:
    print(elem)
    if elem == 100:
        break


squares_list = [num*num for num in range(100_000)]
print(getsizeof(squares_list))
print(type(squares_list))
