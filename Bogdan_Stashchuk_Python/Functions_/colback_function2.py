def send_data(data):
    # sending data to the remote server
    pass


def process_data(input_data, send_data_fn):
    updated_data = input_data.copy()
    # actions with updated_data
    send_data_fn(updated_data)


process_data({'name': 'Oleksandr'}, send_data)
