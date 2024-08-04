from datetime import date


def mult_by_factor(value, multiplier=1):
    return value*multiplier


print(mult_by_factor(2, 10))
print(mult_by_factor(5))

print()
print()


def get_weekday():
    return date.today().strftime('%A')


def create_new_post(post, weekday=get_weekday()):
    post_copy = post.copy()
    post_copy['create_on_weekday'] = weekday
    return post_copy


initial_post = {
    'id': 245,
    'author': 'Oleksandr',
}

post_with_weekday = create_new_post(initial_post)
print(post_with_weekday)
print()
post_with_weekday = create_new_post(post=initial_post, weekday='Monday')
print(post_with_weekday)
