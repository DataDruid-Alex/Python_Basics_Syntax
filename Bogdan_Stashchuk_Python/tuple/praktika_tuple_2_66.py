my_touple = tuple('abcd')
print(my_touple)
my_touple2 = tuple({'first': False, 'second': True})
print(my_touple2)
my_touple3 = tuple([6, 4, 'dfs', 3435, 'dd43ds', True, False])
print(my_touple3)
print()
my_list = ["sav", 353, "rew"]
my_touple4 = tuple(my_list)
print(my_touple4)
my_touple5 = tuple(tuple(my_list[0]) + tuple(my_list[-1]))
print(my_touple5)
my_bool = [True, False]
my_touple6 = tuple(my_bool+my_list)
print(my_touple6)
