my_set = {1, 10, 15}
new_set = set()
for val in my_set:
    new_set.add(val*val)
print('New:', new_set)
print('First set:', my_set)

print("-----other_way-------")
my_set = {1, 10, 15}
new_set = {val*val for val in my_set}
print('New:', new_set)
print('First set:', my_set)

print()

print("----Another example-----")
my_scores = {
    'algebra': 89,
    'physics': 95,
    'english': 70,
}
scores = {}

for k, v in my_scores.items():
    scores[k] = v+5
  #  scores[k] = v*+5
  # {'algebra': 445, 'physics': 475, 'english': 350}
print('Scores:     ', scores)
print("-----other_way-------")
my_scores = {
    'algebra': 89,
    'physics': 95,
    'english': 70,
}
scores = {k: v+5 for k, v in my_scores.items()}

print('Scores:     ', scores)
