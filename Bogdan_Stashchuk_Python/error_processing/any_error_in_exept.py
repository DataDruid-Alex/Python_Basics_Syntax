try:
    # print(10/0)
    # print(10/'0')
    print('10'+0)
    # can only concatenate str (not "int") to str
except Exception as e:
    print(type(e))
    print(isinstance(e, TypeError))
    print(isinstance(e, Exception))
    print(isinstance(e, object))
    print(isinstance(e, str))
    print(e)
print()
try:
    print(10/0)
except:  # not recomend this way
    print("Some error occured")
