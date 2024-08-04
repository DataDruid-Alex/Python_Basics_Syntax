my_name = 'Oleksandr'
my_hobby = 'running'
time = 8
info = my_name+" likes "+my_hobby+" at "+str(time)+' o\'clock'
print(info)
info = f"{my_name} likes {my_hobby} at {str(time)} o'clock"
print(info)
info = f"{my_name.capitalize()} likes {my_hobby.capitalize()} at {
    time} o'clock"
print(info)

print(type(info))

a = True
b = "Brut"
c = "Gordan"
d = 9
e = (20, 53)
print(f"Is {a}? What {b} meet {c} in {d} o'clock. Here {e}!")
