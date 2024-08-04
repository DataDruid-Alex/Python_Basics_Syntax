from pathlib import Path
print(Path('main.py').exists())
print(Path('inp.py').exists())
print(Path('dirrr.py').exists())
print("--------------")

# Windows
# forming new path
print(Path('d:/').joinpath('python').joinpath('module_'))
print(Path('use_my_pack.py').exists())
print()
print("--------------")
p = Path('d:/').joinpath('python').joinpath('module_')
print(p.exists())

print()
print(Path('/python/module_/built_in_modules/use_my_pack.py').exists())
print("Here wats is -_-    :)")
print()
print(Path('module_one.py').exists())
print()
print("is file or directory")

print(Path('main.py').is_file())
print(Path('../json_').is_file())
print(Path('../json_').is_dir())
print(Path.cwd())
print(Path('../Operators_').is_dir())
print(Path('../python').is_dir())
print()
print("-_- ?")


print()
print()
for f in Path('.').iterdir():
    print(f)
