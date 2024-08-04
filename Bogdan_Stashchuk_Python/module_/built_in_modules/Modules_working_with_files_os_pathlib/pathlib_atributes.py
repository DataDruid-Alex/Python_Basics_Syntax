from pathlib import Path
file_path = Path('test.txt')
print([m for m in dir(file_path) if not m.startswith('_')])


print()
print(Path.cwd())
print("-----------")
# Mac and Unix
# forming new path
# print(Path('usr').joinpath('local').joinpath('bin'))
# print(Path('usr')/'local'/'bin')

# Windows
# forming new path
print(Path('d:/').joinpath('python').joinpath('module_'))
