my_motorbike = {
    'brand': 'Ducati',
    'price': 250000,
    'engine_vol': 1.2,
}
# print(my_motorbike['model'])
# KeyError: 'model'
print(my_motorbike.get('model'))
print("NOT KeyError: 'model'")
print(my_motorbike.get('model', "Yeah :) But this Key not exist -_- Try again latter :)"))
print()
print(my_motorbike.get('brand'))
print(my_motorbike.get('price'))
