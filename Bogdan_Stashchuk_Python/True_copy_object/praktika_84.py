from copy import deepcopy

info = {
    'name': 'Oleksandr',
    'is_instructor': False,
    'reviews': []
}

info_copy = info.copy()

info_copy['reviews'].append("Great course!")
info['new_key'] = 990
info_copy['n_key'] = ':)'
print("       _copy_")
print(info_copy)
print()
print(info)

print()
print('     _deep_copy_')

info = {
    'name': 'Oleksandr',
    'is_instructor': False,
    'reviews': []
}

info_deepcopy = deepcopy(info)
info_deepcopy['reviews'].append("Great course!")
info_deepcopy['reviews'].append("-_-")
print(info)
print()

print(info_deepcopy)
