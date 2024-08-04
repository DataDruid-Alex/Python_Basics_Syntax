my_img = ('1920', '1080')
info = f"{my_img[0]}x{my_img[1]}" if len(
    my_img) == 2 else ("Incorect image formating")
print(info)


print("_______________")

if len(my_img) == 2:
    info_if = f"{my_img[0]}x{my_img[1]}"
else:
    info_if = "Incorect image formating"

print(info_if)

print("_______________")
my_str = "kdsfs"
print('my_str:     ', my_str)
my_str = "sssssssssss9ooooooo"
print('my_str:     ', my_str)
my_str = my_img[0]
print('my_str:     ', my_str)
print("String is long") if len(my_str) > 10 else print("String is short")
