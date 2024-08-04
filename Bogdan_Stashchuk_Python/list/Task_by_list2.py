my_list1 = [1, 2, 3]
my_list2 = [10, 20, 30]
print(my_list1)
print(my_list2)
my_merge_list = my_list1+my_list2
print(my_merge_list)
print(dir(list))
my_answer = my_list1.__add__(my_list2)
print(my_answer, "This is method __add__")
