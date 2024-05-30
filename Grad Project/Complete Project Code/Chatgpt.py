from openai import OpenAI
from pathlib import Path

# Set up the client with your API key
client = OpenAI(api_key='')

# Define the path to the newest folder in the 'Finished' directory
finished_dir = Path('/home/ramy/Desktop/folda/Finished')
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

# Path to the newest crash file in the 'crashes' directory
crashes_dir = newest_folder / 'output' / 'default' / 'crashes'
newest_crash_file = max(crashes_dir.iterdir(), key=lambda x: x.stat().st_mtime if x.is_file() else float('-inf'))

# Read the content of the newest crash file in binary mode
with open(newest_crash_file, 'rb') as file:
    binary_content = file.read()

# Convert binary content to a hexadecimal string
crash_content = binary_content.hex()

# Prepare the message to ChatGPT
chat_prompt = (
    f"This is my code:\n{code_content}\n\n"
    f"And this is the input that made it crash:\nCrash Data (hex): {crash_content}\n\n"
    "Suggest me a solution to fix my code using the crash input and the original code."
)

# Set up initial messages for the ChatGPT conversation
messages = [
    {"role": "system", "content": "You are an intelligent assistant."},
    {"role": "user", "content": chat_prompt}
]

# Create the chat completion with ChatGPT based on the full prompt
chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
reply = chat.choices[0].message.content
print(f"ChatGPT: {reply}")

# Save the ChatGPT response to a text file in the same main directory as the crash file (not in 'crashes' subfolder)
output_file_path = newest_folder / 'chatgpt_response.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write(reply)
