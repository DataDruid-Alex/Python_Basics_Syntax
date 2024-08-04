class ExtendedList(list):
    def print_list_info(self):
        print(f"List has {len(self)} elements")


class OneMoreExtendedList(list):
    def print_list_info(self):
        print(f"List has {len(self)} elements")


custom_list = ExtendedList([1, 3, 5, 6, 4])
custom_list.print_list_info()
print(type(custom_list))
custom_list.append(8)
custom_list.print_list_info()
print("-------------")
print(custom_list.__dict__)
print("----ExtendedList----")
print(ExtendedList.__dict__)
print("-------------")
print("----list----")
print(list.__dict__)
print("-------------")
print("----object-----")
print(object.__dict__)
print("-------------")
print("--custom_list--")
print(dir(custom_list))
print("-------------")
print("-------------")
print(list.__subclasses__())
print("-------------")
print("-------------")
print(object.__subclasses__())
# chain class:
# custom_list=>ExtendedList=>list=>object
