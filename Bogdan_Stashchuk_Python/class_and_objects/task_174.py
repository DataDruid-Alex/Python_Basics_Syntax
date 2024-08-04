class Image:
    def __init__(self, s_resolution, s_titile, s_extension):
        self.resolution = s_resolution
        self.title = s_titile
        self.extension = s_extension

    def resize(self, new_resolution):
        self.resolution = new_resolution

    # intresting fiture
    def __str__(self):
        return self.title.capitalize()+self.extension


img1 = Image('1080x1020', 'home', '.jpg')
print(img1.title.capitalize())
print(img1.resolution)
print(img1.extension)
img1.resize('980x1080')
print(img1.resolution, "changed")
print()

img2 = Image('1680x1220', 'trEE', '.png')
print(img2.title.capitalize())
print(img2.resolution)
print(img2.extension)
img2.resize('1080x1680')
print(img2.resolution, "changed")
print()


print("------")
print(img1.__dict__)

print("------")
print(img2.__dict__)


print()
print(dir(img1))

print('----------------')
print('-----Test new fiture----')
print('----------------')

print(img1)  # it is awesome -___- :)
