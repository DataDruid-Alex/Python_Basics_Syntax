my_object = {
    'x': 8,
    'y': 'tireundo',
    'z': False,
}
for item in my_object.items():
    key, value = item
    print(key, value)

print("---------")
for item in my_object.items():
    print(item)

print("---------")

for item in my_object.items():
    k, v = item
    print(k, v)

print("---------")
print("-The best popular iteration syntax -")

for k, v in my_object.items():
    print(k, v)
