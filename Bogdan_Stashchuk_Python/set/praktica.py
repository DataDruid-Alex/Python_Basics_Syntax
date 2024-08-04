photo_demensions = {'1920x1080', '800x600'}
print(len(photo_demensions))
# del photo_demensions[0]
# TypeError: 'set' object doesn't support item deletion

print()
my_set = {10, 10, 5, 15, 15}
print(my_set, "   len =", len(my_set))


# m_set = {(4, [4, 3])}
# TypeError: unhashable type: 'list'

print(type({}))
print(type(set()))
