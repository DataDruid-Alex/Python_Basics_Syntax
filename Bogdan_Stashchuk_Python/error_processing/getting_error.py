try:
    print(10/0)
except ZeroDivisionError as e:  # ErrorType:
    print(type(e))  # <class 'ZeroDivisionError'>
    print()
    print(dir(e))
    print()
    print(e.__str__(), "__str()__")  # print calls __str__()
    print()
    print(e)  # division by zero

print("Continue...")
