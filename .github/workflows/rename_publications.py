import os
import re
import shutil

base_dir = 'content/publication/'

def get_new_folder_name(old_name, existing_names):
    # Extract author, year, and title
    parts = old_name.split('-')
    author = parts[0]
    year = parts[1]
    title = '-'.join(parts[2:])
    # Keep first 3 words of the title
    title_words = re.split('-|_', title)[:3]
    new_title = '-'.join(title_words)
    # Construct new folder name
    new_name = f"{author}-{year}-{new_title}"
    
    # Check for duplicates and add a number if necessary
    count = 1
    original_new_name = new_name
    while new_name in existing_names:
        new_name = f"{original_new_name}-{count}"
        count += 1
    
    existing_names.add(new_name)
    return new_name

existing_names = set()
for folder in os.listdir(base_dir):
    old_folder_path = os.path.join(base_dir, folder)
    if os.path.isdir(old_folder_path):
        new_folder_name = get_new_folder_name(folder, existing_names)
        new_folder_path = os.path.join(base_dir, new_folder_name)
        shutil.move(old_folder_path, new_folder_path)
