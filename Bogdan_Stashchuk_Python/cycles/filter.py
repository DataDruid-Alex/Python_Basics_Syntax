def filter_list(list_to_filter, value_type):
    def check_element_type(elem):
        return type(elem) is value_type
        # return isinstance(elem, value_type)
    return list(filter(check_element_type, list_to_filter))


# without list()
# <filter object at 0x000001FE11DC5D50>
l = [1, (1, 2), 2.1, True, 'periw', 3, 44.9, False, 87, 'sfd']
print(filter_list(l, int))
print("---------")
print(isinstance(True, bool))
print(isinstance(True, int))
print(isinstance(True, object))
print(int.__subclasses__())
