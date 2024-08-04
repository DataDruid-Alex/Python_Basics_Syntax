while True:
    first_num = float(input("Please enter first num: "))
    second_num = float(input("Please enter second num: "))
    if (second_num == 0):
        print("second num can't be 0")
        continue
    print(first_num/second_num)
    answer = input("Do you want to continue? -yes or no? - ")
    if answer == 'no':
        break
    elif answer == 'yes':
        continue
    else:
        "Eror! Value is wrong"
