def mult_by_factor(value, mult=1):
    """Multiplies number by multiplicator"""  # description function
    print(value*mult)
    return value*mult


mult_by_factor(5, 2)


def print_number_info(num):
    """ 
    Prints whether number is even or odd

    Args:
    num(int):Number to be evaluated
    """
    if (num % 2) == 0:
        print("Num is even")
    else:
        print("Num is odd")


print_number_info(21)
print()


def print_number_info(num):
    """_summary_

    Args:   
        num (_type_): _description_
    """
    if (num % 2) == 0:
        print("Num is even")
    else:
        print("Num is odd")
    return (num)


print_number_info(21)
