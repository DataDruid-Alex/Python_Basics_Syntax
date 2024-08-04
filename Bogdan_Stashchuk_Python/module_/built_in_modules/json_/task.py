import json
d = {
    'brand': 'Tesla',
    'price': 68_000,
    'is_avaliable': True,
    'qnt_in_store': 456,
    'qnt_sale': 130,
}
print("----Input dict:")
print(d)
print()
print("Output json str")
print("----JJJ------")
j = json.dumps(d, indent=2)  # easy read
print(j)
print(type(d))


l = [4, None, 5, "dkfd", '__342jd', 3, True, [3, 4]]
print("--l_in_python:--------")
print(l)
print("--l_in_json:--------")
l_in_J = json.dumps(l)
print(l_in_J)
print()
print("-----------")
print("type l_in_J:", type(l_in_J))
