def hi(name):
    print("Hello there,", name)
    print("Hi there,", name)


hi("Oleksandr")
hi("Bogdan")
print(" ")


def sum(a, b):
    sum = a+b
    print(sum)


sum(7, 4)
sum(8.2, 3.3)
sum("asd ", "Basriq")
print(" ")


def sum_numb(a, b):
    return a+b
    print("line is not execute")


su = sum_numb(20, 80)
print(su)
print(" ")
print(sum_numb(98, 23))
print(" ")
print(sum_numb(sum_numb(8, 12), 8))
print(" ")


def errorNoNefunc(a, c):
    sum = a*c


print(errorNoNefunc(1, 3))
print(" ")
print(print("Oleksandr"))
