import string
import re


def is_symbol_contained(word_to_compare, word_to_compare_with, is_bool):
    """
 Checks if any symbol (character) in `word_to_compare` is present in `word_to_compare_with`.

 Args:
     word_to_compare (str): The word to search for symbols within.
     word_to_compare_with (str): The word to check for containing symbols from `word_to_compare`.
     is_bool (bool, optional): A flag indicating the initial state for the return value. Defaults to False.

 Returns:
     bool: True if any symbol in `word_to_compare` is found in `word_to_compare_with`, False otherwise.

 Raises:
     TypeError: If either `word_to_compare` or `word_to_compare_with` is not a string.
 """
    if not isinstance(word_to_compare, str) or not isinstance(word_to_compare_with, str):
        raise TypeError("Both arguments must be strings")

    for symbol in word_to_compare:
        for letter_tocompare_with in word_to_compare_with:
            if symbol == letter_tocompare_with:
                is_bool = True
    return is_bool


def is_valid_password(password):
    """
    Checks if a password meets the following criteria:
    - At least 8 characters long
    - Contains lowercase letters
    - Contains uppercase letters
    - Contains numbers
    - Contains special characters

    Args:
        password (str): The password to be validated.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    is_lowercase_letter = False
    is_uppercase_letter = False
    is_numbers = False
    is_special_characters = False
    if len(password) < 8:
        print(f"You entered {len(password)} characters, you must enter at least 8 characters for the password, add {
              8-len(password)} more characters")

    is_lowercase_letter = is_symbol_contained(
        password, string.ascii_lowercase, is_lowercase_letter)
    is_uppercase_letter = is_symbol_contained(
        password, string.ascii_uppercase, is_uppercase_letter)
    is_numbers = is_symbol_contained(password, string.digits, is_numbers)
    is_special_characters = is_symbol_contained(
        password, string.punctuation, is_special_characters)
    if is_lowercase_letter == False:
        print("The password must contain at least one lowercase letter")
    if is_uppercase_letter == False:
        print("The password must contain at least one uppercase letter")
    if is_numbers == False:
        print("The password must contain at least one digit")
    if is_special_characters == False:
        print("The password must contain at least one special characters")
    if is_lowercase_letter == is_uppercase_letter == is_numbers == is_special_characters == True:
        print("Verification completed successfully! Thank you for your attention!")
        return True
    else:
        print("Try again")
        return False


is_status = False

while (is_status != True):
    user_input_password = input("Please enter your password: ")
    is_status = is_valid_password(user_input_password)
