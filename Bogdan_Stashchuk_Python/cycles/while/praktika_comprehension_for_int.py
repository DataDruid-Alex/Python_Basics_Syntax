my_scores = {
    'algebra': 89,
    'physics': 95,
    'english': 70,
}
scores = {k: v+5 for k, v in my_scores.items()}
scores_set = {v+5 for k, v in my_scores.items()}
scores_list = [v+5 for k, v in my_scores.items()]
print(type(scores_set), scores_set)
print(type(scores_list), scores_list)
print('Scores: ', scores)


print("-----------")
print("-----Another example------")
list_scors1 = [100, 78, 69, 98, 89]
# list_scors2 = {k: v for k, v in enumerate(list_scors1)}
list_scors2 = {index: elem-3 for index, elem in enumerate(list_scors1)}
print(list_scors2)
