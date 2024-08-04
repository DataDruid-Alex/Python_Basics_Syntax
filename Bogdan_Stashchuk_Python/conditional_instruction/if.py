my_number = 39
if my_number > 0:
    print(my_number, "is positive number")

person_info = {
    'age': 20
}
if not person_info.get('name'):
    print('name not exist')


if 10 > 2:
    print(True)


num1 = 10
num2 = 99
# num2 = 99.3

if (
    num1 > 0 and
    num2 > 0 and
    isinstance(num1, int) and
    isinstance(num2, int)
):
    print("Both numbers is ints and positive")
