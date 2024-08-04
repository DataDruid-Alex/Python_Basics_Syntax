ratings = [4, 4.3, 5, 3.2, 3.1, 1, 3, 2, 3.4]
print(ratings, "ratings")
first_two_ratings = ratings[:2]
print(first_two_ratings, "first_two_ratings")
middle_ratings = ratings[1:-1]
print(middle_ratings, " middle")
last_two_ratings = ratings[-2:]
print(last_two_ratings, "  last_two_ratings")
copy_ratings = ratings[:]
print(ratings, "ratings")
print(copy_ratings, "copy_ratings")
print(copy_ratings == ratings)
copy_ratings.sort()
print(ratings, "ratings")
print(copy_ratings, "copy_ratings.sort()")
print(copy_ratings == ratings)
