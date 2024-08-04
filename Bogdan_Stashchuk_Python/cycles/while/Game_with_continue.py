import random
random_num = random.randint(1, 5)
while True:
    num = int(input("Guess the number from 1 to 5: "))
    if num != random_num:
        print("Try again...", f"This number is {random_num}")
        continue
    print("Congratulations!", random_num)
    break
