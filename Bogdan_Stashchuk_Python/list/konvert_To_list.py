greeting = "Hello from Python"
greeting_letters = list(greeting)
print(greeting_letters)
my_dict = {'a': 10, 'b': True}
my_dict_keys = list(my_dict)
print(my_dict_keys)
print(my_dict['a'])
print()
ratings = [3.4, 4.3, 4.5, 4.6, 4.7, 2.9]
print("min =", min(ratings))
print("max =", max(ratings))
print("sum =", sum(ratings))
print("average =", sum(ratings)/len(ratings))

# merge list
print()
my_rating = [3.3, 2.6]
other_rating = [5, 4.5, 3.2, 2.3]
all_rating = my_rating+other_rating
print(all_rating)
