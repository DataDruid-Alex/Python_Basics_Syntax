internal_ids = (321, 432)
external_ids = (563, 233, 121)
print(internal_ids)
print(external_ids)
all_ids = internal_ids+external_ids
print(all_ids)
# magical method+
mag_ids = internal_ids.__add__(external_ids)
print(mag_ids == all_ids)
