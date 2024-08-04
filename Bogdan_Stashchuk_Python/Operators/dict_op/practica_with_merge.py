button_info = {
    'text': 'Buy',
    'colour': "Blue",
    'width': 900,
}
button_style = {
    'colour': "Green",
    'width': 200,
    'height': 300,
}
button_IS = button_info | button_style
button_SI = button_style | button_info

print(button_IS)
print()
print(button_SI)


print()
button_default = {
    'text': 'Ok',
    'colour': "Black",
    'width': 0,
    'height': 0,
}
button_DS = button_default | button_style
button_SD = button_style | button_default

print(button_DS)
print()
print(button_SD)
