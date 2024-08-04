button = {
    'width': 200,
    'text': 'Buy',
}

red_button = {
    **button,
    'colour': 'red'
}

print("red_button:")
print(red_button)
print("button:")
print(button)

print()

grey_button = {
    'width': 200,
    'text': 'Buy',
    'colour': 'grey',
}

red_button = {
    # **grey_button,
    # 'colour': 'red', #This is right

    'colour': 'red',  # attantion on order
    **grey_button,
}

print("red_button:")
print(red_button)
print("grey_button:")
print(grey_button)
