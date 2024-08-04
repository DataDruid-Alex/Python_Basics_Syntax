import zipfile
from pathlib import Path

try:
    # Create the 'my-files' directory if it doesn't exist
    my_files_dir = Path("my-files")
    # Handle nested directories
    my_files_dir.mkdir(parents=True, exist_ok=True)

    # Create the text files with proper paths
    first_file_path = my_files_dir / "first.txt"
    second_file_path = my_files_dir / "second.txt"

    with first_file_path.open('w') as first_file:
        first_file.write("This is the first file.")

    with second_file_path.open('w') as second_file:
        second_file.write("This is the second file.")

except FileExistsError:
    print("Directory 'my-files' already exists.")

# Create the ZIP archive
with zipfile.ZipFile('my-files.zip', mode='w') as my_zip_file:
    print(f"Creating ZIP archive: {Path('my-files.zip').absolute()}")

    # Add files from the directory using Path objects for clarity
    for file_path in my_files_dir.iterdir():
        if file_path.is_file():  # Only add regular files (not directories)
            # Use relative paths for cleaner archive
            my_zip_file.write(file_path, file_path.name)

# Extract the ZIP archive
with zipfile.ZipFile("my-files.zip", mode='r') as my_zip_file:
    print(f"Extracting ZIP archive: {Path('my-files.zip').absolute()}")
    my_zip_file.extractall('my_files_unzipped')

print("ZIP archive creation and extraction completed successfully!")
