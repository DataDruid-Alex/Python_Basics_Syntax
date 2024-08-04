import os
import zipfile


def create_zip(directory, zip_filename):
    """Creates a ZIP archive from the files in the given directory.

    Args:
        directory: The path to the directory containing the files to zip.
        zip_filename: The name of the ZIP file to create.
    """
    try:
        # Create the directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)  # Handle nested directories

        # Create text files within the directory
        first_file_path = os.path.join(
            directory, "Characters from Peter Pen.txt")
        second_file_path = os.path.join(
            directory, "Characters from the Chronicles of Narnia.txt")

        with open(first_file_path, 'w') as first_file:
            first_file.write("""Peter Pan, Tinker Bell, Wendy Moira Angela Darling,
                       Captain Hook, Mr. Smee, John Napoleon Darling, Jack Llewelyn Davies,
                       Michael(Alexander) Nicholas Darling, Nana,
                       George Darling, Mary Darling, Jane, Margaret,
                       Gentleman Starkey, Bill Jukes, Cecco, Cookson, Noodler, 
                       Morgan's Skylights, Black Pirate, Alf Mason, Robert Mullins,
                       George Scourie, Chas. Turley, Foggerty, Alan Herb""")

        with open(second_file_path, 'w') as second_file:
            second_file.write("""Lucy Pevensie, Edmund Pevensie, Peter Pevensie, Susan Pevensie, Prof. Digory Kirke, Eustace Scrubb,
                        Mr. Tumnus, Mr. Beaver, Mrs. Beaver, Trumpkin, Aslan,
                        Father Christmas, Lilliandil, Fox, Oreius,Griffin, King Caspian X.,
                        Maugrim, General Otmin, King Miraz, Reepicheep""")

    except FileExistsError:
        print("Directory '{}' already exists.".format(directory))

    # Create the ZIP archive
    with zipfile.ZipFile(zip_filename, mode='w') as my_zip_file:
        print(f"Creating ZIP archive: {os.path.abspath(zip_filename)}")
        for filename in os.listdir(directory):
            full_path = os.path.join(directory, filename)
            if os.path.isfile(full_path):  # Only add regular files (not directories)
                my_zip_file.write(full_path, os.path.basename(
                    full_path))  # Use relative paths


def extract_zip(zip_filename, extract_dir):
    """Extracts the contents of a ZIP archive to the specified directory.

    Args:
        zip_filename: The path to the ZIP file to extract.
        extract_dir: The directory to extract the files to.
    """
    # Create the extraction directory if it doesn't exist
    os.makedirs(extract_dir, exist_ok=True)  # Handle nested directories

    with zipfile.ZipFile(zip_filename, mode='r') as my_zip_file:
        print(f"Extracting ZIP archive: {os.path.abspath(zip_filename)}")
        my_zip_file.extractall(extract_dir)


# Example usage
create_zip("characters from movies and book", "my-files.zip")
extract_zip("my-files.zip", "characters from movies and book unzipped")

print("ZIP archive creation and extraction completed successfully!")
