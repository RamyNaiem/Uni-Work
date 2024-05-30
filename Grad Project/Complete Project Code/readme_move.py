from pathlib import Path
import shutil
from datetime import datetime

def move_and_rename_readme_and_crash():
    finished_dir = Path('/home/ramy/Desktop/folda/Finished')
    # Identify the newest Fuzz folder
    newest_fuzz_folder = max((folder for folder in finished_dir.iterdir() if folder.is_dir() and 'Fuzz' in folder.name), 
                             key=lambda x: x.stat().st_mtime, default=None)
    
    if newest_fuzz_folder is None:
        print("No Fuzz folder found.")
        return

    # Define the crashes directory path
    crashes_dir = newest_fuzz_folder / 'output' / 'default' / 'crashes'

    # Move README.txt if it exists
    readme_file = crashes_dir / 'README.txt'
    if readme_file.exists():
        destination_path = newest_fuzz_folder / 'README.txt'
        shutil.move(str(readme_file), str(destination_path))
        print(f"README file moved to {destination_path}")
    else:
        print("No README file located in the crashes folder.")

    # Find and rename the crash file
    crash_files = list(crashes_dir.glob('*'))
    if crash_files:
        crash_file = crash_files[0]
        new_name = datetime.now().strftime("%Y%m%d%H%M%S") + '.txt'
        new_crash_file_path = crash_file.parent / new_name
        crash_file.rename(new_crash_file_path)
        print(f"Crash file renamed to {new_crash_file_path}")
    else:
        print("No crash files found in the crashes folder.")

# Call the function
move_and_rename_readme_and_crash()
