def divide_nums(a, b):
    if b == 0:
        # raise TypeError("Second argument can't be zero")
        raise ValueError("Second argument can't be zero")
    return a/b


try:
    divide_nums(22, 0)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
print("Continue...")


print()


try:
    divide_nums(22, 0)
# except ZeroDivisionError as e:
#     print(e) Not possible hapen because we change in VE
except ValueError as e:
    print(e)
print("Continue...")
