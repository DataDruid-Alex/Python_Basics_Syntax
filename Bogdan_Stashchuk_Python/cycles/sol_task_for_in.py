def dict_to_list(dic):
    list_for_convertion = []
    for k, v in dic.items():
        if isinstance(v, int):
            v *= 2
        list_for_convertion.append((k, v))
    return list_for_convertion


d = {'a': 78,
     '5': 98,
     '8': 'dfs'
     }
print(dict_to_list(d))

print("-------2-----")


def filter_list(list_to_filter, value_type):
    filtred_list = []
    for element in list_to_filter:
        # is right way
        # if type(element)==value_type:
        if isinstance(element, value_type):
            # not recomended bool is subclass of int
            filtred_list.append(element)
    return filtred_list


l = [35, True, 'acv', 10]
print(filter_list(l, int))
print(filter_list(l, bool))
# -_- ? -__-
