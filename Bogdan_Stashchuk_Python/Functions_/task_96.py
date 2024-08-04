def merge_lists_to_dict(list_one, list_two):
    merge_dict = dict(zip(list_one, list_two))
    print(merge_dict)
    return merge_dict


merge_lists_to_dict(list_one=['id', 'port', 'type', 'is_conect'],
                    list_two=[1421, 44, 'new', True])

print()
list_one = ['id', 'port', 'type', 'is_conect']

merge_lists_to_dict(list_one,
                    list_two=[1421, 44, 'new', True])

print()
print("Task2")
print()


def update_car_info(**car):

    car_copy = car.copy()
    car_copy['is_avaliable'] = True
    print(car)
    print()
    print(car_copy)
    return car_copy


update_car_info(brand='Tesla', price='69_000')
# update_car_info('Tesla', '69_000')
# TypeError: update_car_info() takes 0 positional arguments but 2 were given
