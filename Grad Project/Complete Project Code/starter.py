import subprocess
import os
from pathlib import Path

def find_executable_in_directory(directory):
    """Find the first file (considered executable) in the specified directory."""
    directory = Path(directory)  # Ensure directory is a Path object
    for file in directory.iterdir():
        if file.is_file() and not file.suffix:  # Assuming the executable has no extension
            return file
    return None

def construct_afl_fuzz_command(input_dir, output_dir, executable):
    """Construct the afl-fuzz command using specified input and output directories, and the executable."""
    # Ensuring absolute paths are used for AFL++ command
    input_dir_abs = os.path.abspath(input_dir)
    output_dir_abs = os.path.abspath(output_dir)
    executable_abs = os.path.abspath(executable)
    return f"afl-fuzz -i {input_dir_abs} -o {output_dir_abs} {executable_abs}"

def run_afl_fuzz_in_konsole(command):
    """Execute the given command in a new Konsole window, with debugging output."""
    print(f"Executing command: {command}")  # Debugging line to print the command
    konsole_command = ["konsole", "--noclose", "-e", "bash", "-c", command]
    subprocess.run(konsole_command)

if __name__ == "__main__":
    # Define the paths using pathlib for consistency
    ongoing_path = Path('ongoing')
    seed_dir = ongoing_path / 'seed'
    output_dir = ongoing_path / 'output'
    code_dir = ongoing_path / 'code'

    os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists

    executable_file = find_executable_in_directory(code_dir)
    if executable_file:
        afl_fuzz_command = construct_afl_fuzz_command(seed_dir, output_dir, executable_file)

        # Debugging: Print the command before executing
        print(f"Command to be executed: {afl_fuzz_command}")

        run_afl_fuzz_in_konsole(afl_fuzz_command)
    else:
        print("Required executable not found.")
