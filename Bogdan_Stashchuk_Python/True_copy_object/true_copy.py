from copy import deepcopy
info = {
    'name': 'Oleksandr',
    'is_instructor': False,
}
info_copy = info.copy()
info_copy['age'] = 20
print(info)
print(info_copy)

print()
print()

info = {
    'name': 'Oleksandr',
    'is_instructor': False,
    'reviews': []
}

info_copy = info.copy()

info_copy['reviews'].append("Great course!")

print(info_copy)
print()
print(info)

print()
print('     deep_copy')

info = {
    'name': 'Oleksandr',
    'is_instructor': False,
    'reviews': []
}

info_deepcopy = deepcopy(info)
info_deepcopy['reviews'] = "Great course!"
print(info)
print()

print(info_deepcopy)
