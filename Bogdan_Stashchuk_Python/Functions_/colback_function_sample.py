def other_fn():
    # some actions
    pass


def fn_with_callback(callback_fn):
    callback_fn()


fn_with_callback()

# fn_with_callback()
# TypeError: fn_with_callback() missing 1 required positional argument: 'callback_fn'
