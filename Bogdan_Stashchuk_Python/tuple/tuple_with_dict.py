users = (
    {
        'user_id': 108,
        'user_name': 'Alice',
    },
    {
        'user_id': 18,
        'user_name': 'Bob',
    }
)
print(users)
print()

print(users[0]['user_id'])

users[0]['user_id'] = 67
print(users[0]['user_id'])
