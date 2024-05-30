import shutil
import os
from pathlib import Path

def move_compiled_file_to_ongoing():
    compiled_dir = Path('compiled')
    target_dir = Path('ongoing/code')

    # Ensure the target directory exists
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # Assuming there's at most one file to move from compiled each time this is run
    for file in compiled_dir.iterdir():
        if file.is_file():
            shutil.move(str(file), str(target_dir / file.name))
            print(f"Moved {file.name} to {target_dir}")
            break  # Assuming only one file is moved at a time



if __name__ == "__main__":
    move_compiled_file_to_ongoing()

