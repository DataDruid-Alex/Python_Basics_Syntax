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
