def validate_args(fn):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise ValueError(f"Type of the {arg} is {type(arg)}",
                                 "All arguments must be int or float!")

        result = fn(*args, **kwargs)
        return result
    return wrapper


@validate_args
def sum_nums(a, b):
    return a+b


try:
    print(sum_nums(7, 4))
    print(sum_nums(17.9, 4.7))
    print(sum_nums('17.9', 4.7))
    # print(sum_nums(a='17.9', b=4.7))
except ValueError as e:
    print(e)

print("Continue...")
# print(sum_nums(7, 4))
# print(sum_nums(17.9, 4.7))


# print(sum_nums('17.9', 4.7))
# ValueError: ("Type of the 17.9 is <class 'str'>", 'All arguments must be int or float!')

# print(sum_nums(a='17.9', b=4.7))
# TypeError: can only concatenate str (not "float") to str
# ValueError: ("Type of the 17.9 is <class 'str'>", 'All arguments must be int or float!')
