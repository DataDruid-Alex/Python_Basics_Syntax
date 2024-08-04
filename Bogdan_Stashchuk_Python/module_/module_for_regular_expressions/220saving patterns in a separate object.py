import re
my_string = "My name is Oleksandr."
res = re.search(r'O........\.$', my_string)
print("res:", res)
my_patern = re.compile(r'O........\.$')
print(my_patern)
print("Patern res:", my_patern.search(my_string))


print()
print()
other_string = "This is strowberry"
string_My = "My favorite fruit is strowberry."
new_patern = re.compile(r"^My.*\.")
print(new_patern.match(my_string))
print(new_patern.match(other_string))
print(new_patern.match(string_My))

patern_for_word = re.compile(r" is ")
print()
print("search word in text where is symbol 'is' :")
print(patern_for_word.findall(other_string))
