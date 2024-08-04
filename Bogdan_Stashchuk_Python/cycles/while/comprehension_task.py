sring_dict = {
    'a': 'algebRa',
    'e': 'engLish',
    'm': 'maTH',
    'p': 'pHySics',
}
corect_string_dict = {k: v.upper() for k, v in sring_dict.items()}
print('    corect_string_dict')
print(corect_string_dict)
print()
print('     sring_dict')
print(sring_dict)

print()
print("        ----___Task2___-----")

l1 = ['a', 'hk', 'fdf', 'sage', 'water', 'hong', 'honey', 'ls', 'cmd']
l2 = [l for l in l1 if len(l) > 3]
print('List one', l1)
print('List two', l2)
