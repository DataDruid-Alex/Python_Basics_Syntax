goods = ['arm', 'sofa', 'chair', 'bed', 'shelf']
price = [1000, 20_000, 800, 40_000, 23_000]
goods_price_zip = zip(goods, price)
print(goods, 'goods')
print(price, 'price')
print(goods_price_zip)
print()
l = t = d = goods_price_zip
goods_price_list = list(l)
goods_price_tuple = tuple(t)
goods_price_dict = dict(d)

print(goods_price_list)
print()
print(goods_price_tuple)
print(goods_price_dict)
# ?????????????????????????
