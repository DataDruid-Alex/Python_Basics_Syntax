def increase_person_age(person):
    person_copy = person.copy()
    person_copy['age'] += 1
    print(person, 'person')
    print()
    print(person_copy, 'person_copy')
    return person_copy


person_one = {
    'name': 'Oleksandr',
    'age': 20
}

new_person = increase_person_age(person_one)
print(person_one, 'person external')
print(id(person_one), 'id person external')
print()
print(new_person, 'person change in function')
print(id(new_person), 'id sperson change in function')
