def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        info = "Here is one argument with not intiger"
    elif a >= b:
        info = f"{a} greater or equal than {b}"
    else:
        info = f"{a} less than {b}"
    return info

# def nums_info(a, b):
#     if (type(a) is not int) or (type(b) is not int):
#         return "Here is one argument with not intiger"
#     if a >= b:
#         return f"{a} greater or equal than {b}"
#     return f"{a} less than {b}"


print(nums_info(3, 4))
print(nums_info(90, 44))
print(nums_info(44, 44))
print(nums_info(True, 44))
