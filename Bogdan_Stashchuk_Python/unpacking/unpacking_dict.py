user_profile = {
    'name': "Oleksandr",
    'coments_qnt': 53,
}


def user_info(name, coments_qnt=0):
    if not coments_qnt:
        return f"{name} has no comments"

    return f"{name} has {coments_qnt} comments"


print(user_info(**user_profile))
# Oleksandr has 53 comments
print()
print(user_profile)
print()
print('______________________________')

print(user_info(user_profile))
print('______________________________')

print(user_info(user_profile['name'], user_profile['coments_qnt']))
print('______________________________')

print(user_info(name=user_profile['name'],
      coments_qnt=user_profile['coments_qnt']))
print()
print('-_-')
name, com_qty = user_profile
print(name)
print(com_qty)  # qty=qnt     get keys dict
