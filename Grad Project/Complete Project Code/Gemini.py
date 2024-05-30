import google.generativeai as genai
import os
from google.generativeai import GenerativeModel
from pathlib import Path

# Set the API key directly in the script
api_key = ""
genai.configure(api_key=api_key)

# Absolute path to the 'Finished' directory
finished_dir = Path('/home/ramy/Desktop/folda/Finished')

# Ensure the 'Finished' directory exists and is not empty
if not finished_dir.exists() or not any(finished_dir.iterdir()):
    print("No 'Finished' directory or it is empty.")
    exit()

# Find the newest folder in the 'Finished' directory
newest_folder = max(finished_dir.iterdir(), key=lambda x: x.stat().st_mtime if x.is_dir() else float('-inf'))

# Find the first .c or .cpp file in the newest folder
code_files = list(newest_folder.glob('*.c')) + list(newest_folder.glob('*.cpp'))
if not code_files:
    print("No code files found in the newest folder.")
    exit(1)
code_file = code_files[0]

# Read the content of the code file
with open(code_file, 'r') as file:
    code_content = file.read()

# Path to the 'crashes' directory in the newest folder
crashes_dir = newest_folder / 'output' / 'default' / 'crashes'

# Ensure the 'crashes' directory exists and contains files
if crashes_dir.exists() and any(crashes_dir.iterdir()):
    # Find the newest file in the 'crashes' directory
    newest_file = max(crashes_dir.iterdir(), key=lambda x: x.stat().st_mtime if x.is_file() else float('-inf'))
    
    # Read the content of the newest crash file in binary mode
    with open(newest_file, 'rb') as file:
        binary_content = file.read()

    # Convert binary content to a hexadecimal string (as an example)
    crash_content = binary_content.hex()

    # Use the content in the AI model
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    prompt = (
        f"This is my code:\n{code_content}\n\n"
        f"And this is the input that made it crash:\nCrash Data (hex): {crash_content}\n\n"
        "Suggest me a solution to fix my code using the crash input and the original code."
    )
    response = model.generate_content(prompt)
    
    # Save the AI's response
    response_path = newest_folder / 'Ai_response.txt'
    with open(response_path, 'w') as file:
        file.write(response.text)
    print(f"AI Response saved to {response_path}")

else:
    print("No 'crashes' directory found or it is empty.")
