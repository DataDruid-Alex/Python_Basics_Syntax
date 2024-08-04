def log_function_call(original_fn):
    def wrapper(*args, **kwargs):
        print(f"Function name: {original_fn.__name__}")
        print(f"Function arguments: {args},{kwargs}")

        result = original_fn(*args, **kwargs)

        print(f"Function result: {result}")
        return result
    return wrapper


@log_function_call
def mult(a, b):
    return a*b


@log_function_call
def sum(a, b):
    return a+b


print(mult(3, 4))
print()
print(mult(a=3, b=4))

print("---------")
print()
print(sum(67, 3))

print()
print(sum(a=77, b=13))
