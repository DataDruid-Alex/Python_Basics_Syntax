photo_demensions = {'1920x1080', '800x600'}
print(photo_demensions)
print(len(photo_demensions))
photo_demensions.add('1024x768')
print(photo_demensions)
print(len(photo_demensions))

print()
# union()
photo_sizes = {'1920x1080', '800x600'}
other_sizes = {'800x600', '1024x768'}
# all_sizes = photo_sizes+other_sizes
# print(all_sizes)
# TypeError: unsupported operand type(s) for +: 'set' and 'set'
all_sizes = photo_sizes.union(other_sizes)
print(all_sizes, "with union methods")
a_sizes = photo_sizes | other_sizes
print(a_sizes, " with | operator")

print()
# intersection()
common_s = photo_sizes.intersection(other_sizes)
print(common_s)
com_with_op = photo_sizes & other_sizes
print(com_with_op)
# issubset
print()
nums = {1, 2, 3, 4, 5}
other_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
res = nums.issubset(other_nums)
print(res)

print(nums.issuperset(other_nums), "Issuperset?")
print(other_nums.issuperset(nums), "Issuperset?")
