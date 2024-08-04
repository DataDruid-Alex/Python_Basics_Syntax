import string
import re
# test_password = "dkfs8898989"


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
    length_pattern = re.compile(r"\S{8,}")
    lowercase_pattern = re.compile(r"^.*[a-z]+.*$")
    uppercase_pattern = re.compile(r"^.*[A-Z]+.*$")
    number_pattern = re.compile(r"^.*[0-9]+.*$")
    special_symbol_pattern = re.compile(r"^.*[-!@#$%^&*\.]+.*$")
    no_white_space_pattern = re.compile(r"^\S*$")
    if not re.fullmatch(no_white_space_pattern, password):
        return (False, "No whitespaces allowed in the password")
    if not re.fullmatch(length_pattern, password):
        return (False, "Password must have at least 8 symbols")
    if not re.fullmatch(lowercase_pattern, password):
        return (False, "The password must contain at least one lowercase letter")
    if not re.fullmatch(uppercase_pattern, password):
        return (False, "The password must contain at least one uppercase letter")
    if not re.fullmatch(number_pattern, password):
        return (False, "The password must contain at least one digit")
    if not re.fullmatch(special_symbol_pattern, password):
        return (False, "The password must contain at least one special characters -!@#$%^&*.")
    return (True, "Verification completed successfully! Thank you for your attention!")


# print(is_valid_password("SA   adfs9ff-    sf"))
# print(is_valid_password("12323"))
# print(is_valid_password("12322333024993"))
# print(is_valid_password("90989d3afd"))
# print(is_valid_password("SAadfsdffdsf"))
# print(is_valid_password("SAadfs9ffdsf"))
# print(is_valid_password("SAadfs9ff-sf"))
while True:
    input_password = input("Please enter password: ")
    password_check_res = is_valid_password(input_password)
    if password_check_res[0]:
        print(password_check_res[1])
        break
    password_check_res[1]
