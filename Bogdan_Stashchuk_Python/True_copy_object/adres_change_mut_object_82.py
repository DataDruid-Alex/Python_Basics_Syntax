my_list = [1, 2, 3]
print(id(my_list))
other_list = [1, 2, 3]
print(id(other_list))
print(id([1, 2, 3]))

other_list.append(99)
print(my_list, id(my_list))
print(other_list, id(other_list))

print()
a = b = [3, 21, 5]
print(a, id(a), 'a')
print(b, id(b), 'b')

print()
a.append(my_list)
print(a, id(a), 'a')
print(b, id(b), 'b')

info = {
    'name': 'Oleksandr',
    'is_instructor': False,
}
info_copy = info
info_copy['age'] = 20
print(id(info), 'info', info)
print(id(info_copy), 'copy', info_copy)

my_inf = {
    'name': 'Oleksandr',
    'is_instructor': False,
}
other_inf = {
    'name': 'Oleksandr',
    'is_instructor': False,
}
print(id(my_inf), 'my')
print(id(other_inf), 'other')
my_inf['age'] = 20
other_inf['job'] = 'poor student'
print()
print(my_inf, 'my', id(my_inf))
print()

print(other_inf, 'other', id(other_inf))
