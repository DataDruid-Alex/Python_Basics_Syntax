image_info = {
    'image_id': 3443,
    'image_title': "this is Watermelon",
    'image_size': '1080x1640',
    'date_add': '20/09/2005',
}


def get_image_id_and_title(dict):
    if ('image_id' not in image_info.keys()):
        raise TypeError("Not image_id. Enter image_id")
    if ('image_title' not in image_info.keys()):
        raise TypeError("Not image_title.Enter image_title")
    return f"Image {dict['image_title']} has id {dict['image_id']}"


info = get_image_id_and_title(image_info)
print(info)

print()

try:
    del image_info['image_id']
    info = get_image_id_and_title(image_info)
    print(info)
except TypeError as t:
    print(t)
finally:
    image_info['image_id'] = 4590
print("Continue...")

print()

try:
    del image_info['image_title']
    info = get_image_id_and_title(image_info)
    print(info)

except TypeError as t:
    print(t)
finally:
    image_info['image_title'] = "my cat"
print("Continue...")
print()

print(image_info)
