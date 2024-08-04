def merge_lists_to_dict(l1, l2):
    merge = zip(l1, l2)
    merge_dict = dict(merge)
    print(merge_dict)
    return merge_dict


l1 = ['id', 'port', 'type', 'is_conect']
l2 = [1421, 44, 'new', True]
merge_lists_to_dict(l1, l2)
