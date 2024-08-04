def filter_list(list_to_filter, value_type):
    return list(filter(lambda elem: type(elem) is value_type, list_to_filter))


l = [1, (1, 2), 2.1, True, 'periw', 3, 44.9, False, 87, 'sfd']
print(filter_list(l, int))
