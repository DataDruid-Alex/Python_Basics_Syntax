# my_fruits = ['mango', 'kiwi', 'strowberry', 'lime']
my_fruits = ('mango', 'kiwi', 'strowberry', 'lime')
mango, *remain_fruits = my_fruits
print(mango)
print(remain_fruits, type(remain_fruits))  # why is list??????????
