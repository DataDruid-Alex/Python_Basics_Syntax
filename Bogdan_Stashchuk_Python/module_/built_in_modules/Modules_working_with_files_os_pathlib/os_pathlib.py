from pathlib import Path
from os import path

print(path.abspath('.'))
print(type(path))

print("--------------")

print(Path('.').absolute())
print(type(Path))
