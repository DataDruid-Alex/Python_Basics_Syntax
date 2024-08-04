def image_info(img):
    if ('image_id' not in img) or ('image_title' not in img):
        raise TypeError("Keys image_id and image_title must be present")
    return f"Image {img['image_title']} has id {img['image_id']}"


print(image_info({'image_title': "my cat", 'image_id': 3432}))
# print(image_info({'image_id': 3432}))
# TypeError: Keys image_id and image_title must be present

# print(image_info({'image_title': "my cat"}))
# TypeError: Keys image_id and image_title must be present
try:
    print(image_info({'image_title': "my cat"}))
except TypeError as t:
    print(t)
