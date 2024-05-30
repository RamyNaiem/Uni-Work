import os
import shutil

def create_and_get_fuzz_folder(finished_path):
    """Create a new Fuzz folder based on existing ones to avoid name conflicts."""
    i = 1
    while True:
        fuzz_folder_name = f"Fuzz{i}"
        fuzz_folder_path = os.path.join(finished_path, fuzz_folder_name)
        if not os.path.exists(fuzz_folder_path):
            os.makedirs(fuzz_folder_path)
            return fuzz_folder_path
        i += 1

def move_contents(source_path, destination_path):
    """Move all contents from source to destination."""
    for item in os.listdir(source_path):
        item_path = os.path.join(source_path, item)
        shutil.move(item_path, destination_path)

def move_new_files_to_fuzz(new_folder_path, destination_path):
    """Move files from 'new' folder to the newest Fuzz folder."""
    move_contents(new_folder_path, destination_path)

def main():
    ongoing_path = 'ongoing'
    finished_path = 'Finished'
    code_path = os.path.join(ongoing_path, 'code')
    seed_path = os.path.join(ongoing_path, 'seed')
    output_path = os.path.join(ongoing_path, 'output')
    new_path = 'new'  # Path to the 'new' folder

    # Ensure the Finished folder exists
    if not os.path.exists(finished_path):
        os.makedirs(finished_path)

    # Handle the output folder and rename to avoid conflicts
    fuzz_folder_path = create_and_get_fuzz_folder(finished_path)
    shutil.move(output_path, fuzz_folder_path)  # Move and rename output to FuzzX

    # Move contents of code, seed, and new to the new Fuzz folder
    move_contents(code_path, fuzz_folder_path)
    move_contents(seed_path, fuzz_folder_path)
    move_new_files_to_fuzz(new_path, fuzz_folder_path)

if __name__ == "__main__":
    main()
