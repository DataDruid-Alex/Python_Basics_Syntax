my_motorbike = {
    'brand': 'Ducati',
    'price': 250000,
    'engine_vol': 1.2,
}
print(my_motorbike)
print(my_motorbike['brand'])
print(my_motorbike['price'])
my_motorbike['price'] = 270210
print()
print(my_motorbike, "change price")
my_motorbike['is_new'] = True
print()
print(my_motorbike)

del my_motorbike['engine_vol']
print()
print(my_motorbike)
