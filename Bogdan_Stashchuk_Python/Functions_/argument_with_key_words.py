def get_posts_info(name, posts_qnty):
    info = f"{name} wrote {posts_qnty} posts"
    return info


info = get_posts_info(name='Oleksandr', posts_qnty=100)
print(info)

info = get_posts_info(posts_qnty=100, name='Oleksandr')
print(info)
info = get_posts_info(100, 'Oleksandr')
print(info)
