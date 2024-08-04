my_motorbike = {
    'brand': 'Ducati',
    'price': 250000,
    'engine_vol': 1.2,
}
print(my_motorbike)
other_motorbike = {
    'engine_vol': 1.2,
    'price': 250000,
    'brand': 'Ducati',
}
print(other_motorbike)
print(my_motorbike == other_motorbike)
print(id(my_motorbike) == id(other_motorbike))
