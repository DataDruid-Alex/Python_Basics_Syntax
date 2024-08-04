fruits = ['apple', 'banana', 'lime', 'orange']
quantities = {100, 50, 32, 55}  # -_- random position because is set

avaliability = (True, False, True, True)
fruit_quant_zip = zip(fruits, quantities, avaliability)
# <zip object at 0x000001C953B73C00>
print(fruit_quant_zip, type(fruit_quant_zip))
print()
fruit_quant_list = list(fruit_quant_zip)
print(fruit_quant_list)


print()
print('new')
fruits = ['apple', 'banana', 'lime', 'orange']
quantities = '9394'  # -_- random position because is set

avaliability = (True, False, True, True)
fruit_quant_zip = zip(fruits, quantities, avaliability)
# <zip object at 0x000001C953B73C00>
print(fruit_quant_zip, type(fruit_quant_zip))
print()
fruit_quant_list = list(fruit_quant_zip)
print(fruit_quant_list)
