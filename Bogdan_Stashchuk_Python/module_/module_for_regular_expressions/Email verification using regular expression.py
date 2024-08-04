import re
# email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
# email_check_patern = re.compile(email_regexp)
# # Valid
# print(email_check_patern.fullmatch('avd@gmail.com'))
# print(email_check_patern.fullmatch('a_vd@gmail.com'))
# print(email_check_patern.fullmatch('a.vd@sub.gaiul.com'))
# print(email_check_patern.fullmatch('avd@gmail.com'))
# # Invalid
# print(email_check_patern.fullmatch('@gmail.com'))
# print(email_check_patern.fullmatch('avd@gmailcom'))
# print(email_check_patern.fullmatch('avd@gmail.'))
# print(email_check_patern.fullmatch('avd-gmail.com'))


def check_email(email):
    email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    email_check_patern = re.compile(email_regexp)
    validation_result = "valid" if email_check_patern.fullmatch(
        email) else "not valid"
    return (email, validation_result)


# Valid
print(check_email('avd@gmail.com'))
print(check_email('a_vd@gmail.com'))
print(check_email('a.vd@sub.gaiul.com'))
print(check_email('avd@gmail.com'))
# Invalid
print(check_email('@gmail.com'))
print(check_email('avd@gmailcom'))
print(check_email('avd@gmail.'))
print(check_email('avd-gmail.com'))
