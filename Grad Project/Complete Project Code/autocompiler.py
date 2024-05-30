import subprocess
from pathlib import Path
from shutil import move

# Configuration
waiting_dir = Path('/home/ramy/Desktop/folda/waiting')  # Directory with C/C++ files
compiled_dir = Path('/home/ramy/Desktop/folda/compiled')  # Destination for executables
new_dir = Path('/home/ramy/Desktop/folda/new')  # Destination for the newest source file

# Ensure directories exist
compiled_dir.mkdir(parents=True, exist_ok=True)
new_dir.mkdir(parents=True, exist_ok=True)

def compile_source(source_path):
    """
    Compiles a given source file with AFL++'s gcc or g++.
    The compiled executable is placed in the compiled_dir.
    """
    compiler = 'afl-g++' if source_path.suffix == '.cpp' else 'afl-gcc'
    output_path = compiled_dir / source_path.stem  # Executable name based on source file

    # Compilation command
    compile_command = [compiler, str(source_path), '-o', str(output_path)]

    # Execute the compilation command
    result = subprocess.run(compile_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"Compiled {source_path.name} successfully.")
        return True
    else:
        print(f"Failed to compile {source_path.name}. Error:\n{result.stderr.decode()}")
        return False

def move_newest_file():
    """
    Moves the newest source file from the waiting directory to the new directory.
    """
    try:
        newest_file = max(waiting_dir.iterdir(), key=lambda x: x.stat().st_mtime)
        move(str(newest_file), str(new_dir / newest_file.name))
        print(f"Moved {newest_file.name} to {new_dir}.")
    except ValueError:
        print("No files to move.")

def main():
    # Move the newest file and compile it
    move_newest_file()
    newest_file_path = new_dir / max(new_dir.iterdir(), key=lambda x: x.stat().st_mtime).name
    compile_source(newest_file_path)

if __name__ == "__main__":
    main()
