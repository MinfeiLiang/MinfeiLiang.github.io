import os
import re
import shutil

base_dir = 'content/publication/'

def get_new_folder_name(old_name):
    parts = old_name.split('-')
    if len(parts) < 3:
        # Skip folders that do not match the expected pattern
        print(f"Skipping folder with unexpected name format: {old_name}")
        return old_name
    author = parts[0]
    year = parts[1]
    title = '-'.join(parts[2:])
    # Construct new folder name
    new_name = f"{author}-{year}-{title}"
    return new_name

for folder in os.listdir(base_dir):
    old_folder_path = os.path.join(base_dir, folder)
    if os.path.isdir(old_folder_path):
        new_folder_name = get_new_folder_name(folder)
        if new_folder_name != folder:
            new_folder_path = os.path.join(base_dir, new_folder_name)
            # Check if the new folder path already exists to avoid collision
            if not os.path.exists(new_folder_path):
                shutil.move(old_folder_path, new_folder_path)
            else:
                print(f"Skipping rename to avoid collision: {new_folder_path}")
