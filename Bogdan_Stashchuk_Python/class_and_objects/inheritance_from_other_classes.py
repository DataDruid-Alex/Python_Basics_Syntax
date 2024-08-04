class ExtendedList(list):
    def print_list_info(self):
        print(f"List has {len(self)} elements")


custom_list = ExtendedList([1, 3, 5, 6, 4])
custom_list.print_list_info()


# chain class:
# custom_list=>ExtendedList=>list=>object
