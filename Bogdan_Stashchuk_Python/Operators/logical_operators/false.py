print(bool(int(0)))
print(bool(float(0.0)))
print(bool(complex(0j)))
print()
print(bool(0))
print(bool(0.0))
print(bool(0j))

print(bool(None))
# =>
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(set()))
print(bool(range(0)))
print(bool(""))
print(type({}))
print(not not bool('a'))
print(not not bool(""))
print(not not bool([]))
print(not not bool(()))


my_list = [1, 2]
if len(my_list) > 0:
    print("List has element")
print(len(my_list) > 0)
print("_________Identical condition____")
if my_list:
    print("List has element")
print(bool(my_list))
