my_list = [['first', 'Anime'], ['second', 'manga'], [
    'third', 'manxia'], ['four', 'ranobe'], ['five', 'web_novel']]
my_dict = dict(my_list)
print(my_dict)
print()
print()

my_list = [('first', 'Anime'), ('second', 'manga'),
           ('four', 'ranobe'), ['five', 'web_novel']]
# (),(),(),[]=good work
my_dict = dict(my_list)
print(my_dict)

print()
new_list = [[1, 'first'], [2, True], [0, False], [777, 12]]
new_dict = dict(new_list)
print(new_dict)
