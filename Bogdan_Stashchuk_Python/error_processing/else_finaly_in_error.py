try:
    print(10/5)
except ZeroDivisionError as e:  # ErrorType:
    print(e)  # division by zero
except TypeError as e:
    print(e)  # unsupported operand type(s)
    # for /: 'str' and 'int'
else:  # if only not error
    print("There was no error")

print("Continue...")


print()
try:
    print(10/5)
except ZeroDivisionError as e:  # ErrorType:
    print(e)  # division by zero
except TypeError as e:
    print(e)  # unsupported operand type(s)
    # for /: 'str' and 'int'
else:  # if only not error
    print("There was no error")
finally:  # Anyway
    print("Continue...")  # Continue
