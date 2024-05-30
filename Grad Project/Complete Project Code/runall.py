import subprocess

def run_script(script_name):
    """Runs a Python script and waits for it to complete."""
    print(f"Starting {script_name}...")
    try:
        # Using check=True to ensure any error raises an exception
        subprocess.run(['python3', script_name], check=True)
        print(f"Finished running {script_name} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while running {script_name}: {e}")

if __name__ == "__main__":
    scripts_to_run = [
        'downloader.py',   # Ensure this script is first to fetch and prepare files
        'autocompiler.py',
        'analyzer.py',
        'mover.py',
        'starter.py',
        'Finished_mover.py',
        'readme_move.py',
        'Gemini.py',
        'Chatgpt.py',
        'pdfmaker.py'
    ]

    for script in scripts_to_run:
        run_script(script)
