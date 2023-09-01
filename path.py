from pathlib import Path
import glob
import os

relative_path = "cache"
prefix = "Bao - 52-Hearts [1 Hour Loop]"

absolute_path = os.path.abspath(relative_path)
matching_files = [file for file in os.listdir(absolute_path) if file.startswith(prefix)]

print('list_files: ', matching_files)

# # Example path
# path_with_directory = "cache/Bao - 52-Hearts [1 Hour Loop].m4a"

# # Create a Path object
# path_obj = Path(path_with_directory)

# # Extract the file name using Path.name
# file_name = path_obj.name

# print(file_name)  # Output: filename.txt