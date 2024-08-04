from zipfile import ZipFile
from pathlib import Path

# with ZipFile("my-files.zip", mode='r') as my_zip_file:
#     my_zip_file.extractall('my_files_unzipped')
#     print(Path("my-files.zip").absolute())
#     print(Path().absolute())
#     print(my_zip_file.infolist())


# Extract the ZIP archive

with ZipFile("my-files.zip", mode='r') as my_zip_file:
    print(f"Extracting ZIP archive: {Path('my-files.zip').absolute()}")
    my_zip_file.extractall('my_files_unzipped')

print("ZIP archive creation and extraction completed successfully!")
