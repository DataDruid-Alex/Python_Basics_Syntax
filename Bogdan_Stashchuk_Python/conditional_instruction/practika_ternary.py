my_img = ('1920', '1080')
# my_img = ('1920', '1080', True)
print(f"{my_img[0]}x{my_img[1]}") if len(
    my_img) == 2 else print("Incorect image formating")

info = f"{my_img[0]}x{my_img[1]}" if len(
    my_img) == 2 else ("Incorect image formating")
print(info)
