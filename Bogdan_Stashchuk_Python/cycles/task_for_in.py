def dict_to_list(dic):
    for k in dic:
        if isinstance(dic[k], int):
            dic[k] *= 2
    lis = list(dic.items())
    return lis


d = {'a': 78,
     '5': 98,
     '8': 'dfs'
     }
print(dict_to_list(d))

print("-----2---------")


def filter_list(a_list, types):
    n = []
    for a in a_list:
        n.append(a) if types == type(a) else True
    return n


l = [1, 2, 3, 'q', 'r', "uno", (3, 2), 6, 0, -2,
     (-2, '8od', True), False, True, True]
print(filter_list(l, bool))
