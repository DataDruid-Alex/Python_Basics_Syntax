def route_info(a_dict):
    if a_dict.get('distance') and isinstance(a_dict['distance'], int):
        return f"Distance to your destination is {a_dict['distance']})"
    elif a_dict.get('speed') and a_dict.get('time'):
        return f"Distance to your destination is {a_dict['speed']*a_dict['time']}"

    else:
        return "No distance is available"


my_dict = {
    # 'distance': 68,
    'speed': 15,
    # 'time': 3,
}
print(route_info(my_dict))
