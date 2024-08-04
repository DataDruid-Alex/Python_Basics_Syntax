def get_posts_info(**person):
    print(person)
    print(type(person))

    info = (
        f"{person['name']} wrote "
        f"{person['posts_qnty']} posts"
        #   f"{person.get('posts_qnty')} posts"
    )  # automatik merge two str in one str
    return info


info = get_posts_info(name='Oleksandr', posts_qnty=100)
info = get_posts_info(name='Oleksandr', posts_qnty=100, id=333)
# info = get_posts_info(name='Oleksandr', posts=100)
# KeyError: 'posts_qnty'
# info = get_posts_info('Oleksandr', 100)
# TypeError: get_posts_info() takes 0 positional arguments but 2 were given
print(info, type(info))
