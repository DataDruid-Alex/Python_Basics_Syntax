from pathlib import Path
from zipfile import ZipFile
import os

try:
    os.mkdir("my-files")
    with open("my-files/first.txt", 'w') as my_file:
        my_file.write("This is first file")
    with open("my-files/second.txt", 'w') as my_file:
        my_file.write("This is second file")
except FileExistsError:
    print("Directory 'my-files' already exists.")
    print()

with ZipFile('my-files.zip', mode='w') as my_zip_file:
    print(my_zip_file)

directory = "my-files"

for filename in os.listdir(directory):
    full_path = os.path.join(directory, filename)
    print(full_path)
    # my_zip_file.write(full_path)

print()
print()
# if use class Path

for file in Path(directory).iterdir():
    print(file)
    my_zip_file.write(full_path)
