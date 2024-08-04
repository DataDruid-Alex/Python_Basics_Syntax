from pathlib import Path
print("-----------------------")
with open('test.txt') as test_file:
    print(test_file.read())
print("---------------")
with open('test.txt') as test_file:
    print(test_file.readlines())
print("----------------")

print("--------write------")
with open('new.txt', 'w') as new_file:
    new_file.write("First line in the new file\n")

print("--add_to_file_some_text--")

with open('new.txt', 'a') as new_file:
    new_file.write("Second line in the new file\n")
print("------read------")

with open('new.txt') as new_file:
    print(new_file.read())
print("-----delete file-------")
print(Path('new.txt').exists())
Path('new.txt').unlink()
print(Path('new.txt').exists())
# delete file
