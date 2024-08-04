from pathlib import Path
from os import path
print(path.curdir)
print(path.abspath('.'))
print(type(Path))
cwd = Path('.')
print(cwd)
print(isinstance(cwd, Path))
print(type(cwd))
print("------")
print(Path.__subclasses__())
print("-------------")
print(dir(cwd))
print("-------------")
print(cwd.absolute())
print(Path('d:/').joinpath('python/'))
print("-_- ------------------")
print()
print("---Crazy code!!!! Necessary---")
# new_dir = Path('d:/').joinpath('python/newdirectory')
# if not new_dir.exists():
#     new_dir.mkdir()
# if new_dir.exists():
#     new_dir.rmdir()

print("This is succesful!!!!___mkdir()")
print(Path('d:/')/'Numbers'/'complex')
