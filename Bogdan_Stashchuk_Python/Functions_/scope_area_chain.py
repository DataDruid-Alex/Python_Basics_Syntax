a = 5


def my_fn():
    def inner_fn():
        print(a)
        # a = 10
        # UnboundLocalError: cannot access local variable 'a'
        # where it is not associated with a value
    inner_fn()


my_fn()
