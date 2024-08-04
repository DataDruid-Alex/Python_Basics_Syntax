# print(10/0)
# ZeroDivisionError: division by zero
# print("Continue...")


try:
    pass
except ZeroDivisionError:  # ErrorType:
    pass
# ErrorType


try:
    print(3/1)
    # print(3+'1')
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
    print(10/0)
    print(9/2)
except ZeroDivisionError:  # ErrorType:
    print("Eror - Division by zero")

print("Continue...")
print(type(ZeroDivisionError))
print(ZeroDivisionError)
print(type(int))
