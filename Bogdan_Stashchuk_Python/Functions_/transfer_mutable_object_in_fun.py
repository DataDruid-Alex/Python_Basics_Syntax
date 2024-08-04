def increase_person_age(person):
    print(id(person), 'id dict_fun before age change')
    person['age'] += 1
    print(id(person), 'id dict_fun, after')
    print()
    print(person)
    print(type(person))
    return person


person_one = {
    'name': 'Oleksandr',
    'age': 20
}
print(id(person_one), 'id person_one before func_')
print()
increase_person_age(person_one)
print()
print(id(person_one), 'id person_one after func_')
print(person_one['age'])
