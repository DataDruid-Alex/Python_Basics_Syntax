print(bool(10))
print(bool('abs'))
print(bool([]))
print(bool([1, 2, 3]))
print(bool(None))

print()
db_is_available = False
print(db_is_available, type(db_is_available))
db_is_available = True
print(db_is_available, "db_is_available")

print([] == [])
print([1, 5, 7, 2] == [1, 2, 7, 5])
print({'a': 5} == {'a': 5}, "dict")
print({'a': 2} == {'a': 5}, "dict")
print({'a': 5} == {'b': 5}, "dict")
