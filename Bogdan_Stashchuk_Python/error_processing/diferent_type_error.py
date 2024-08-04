try:
    print(10/0)
except ZeroDivisionError as e:  # ErrorType:
    print(isinstance(e, Exception))
    print(e)  # division by zero
except TypeError as e:
    print(e)  # unsupported operand type(s)
    # for /: 'str' and 'int'

print("Continue...")
