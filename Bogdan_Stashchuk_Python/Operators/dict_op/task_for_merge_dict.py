default_TV = {
    'brand': 'Name brand',
    'size': "32in-98in",
    "resulution": "SD,HD,FHD,UHD(4K),8K",
    "type matrix": "LED, QLED,Nano Cell",
    'is_smart_TV': "True or False",
    "purchase_price": 0,
    "item_price": 0,
    "is_available_in_store": "True or False",
    "is_available_in_supplier": "True or False",
}
shop_TV = {
    'brand': 'Sony',
    'size': "64in",
    "resulution": "UHD(4K)",
    "type matrix": 'LED',
    'is_smart_TV': True,
    "purchase_price": 800,
    "item_price": 1000,
    "is_available_in_store": True,
    "is_available_in_supplier": False,
}
customer_TV = {
    "purchase_price": None,
    "is_available_in_supplier": None,

    'name_customer': "Bogdan",
    "age_customer": 34,
}
# customer_TV.pop(customer_TV.items)
merge_three_dict = default_TV | shop_TV | customer_TV
print(merge_three_dict)
