import clang.cindex
from clang.cindex import Index, TokenKind
import re
import os

# Define the directory containing your .c or .cpp files here
DIRECTORY = "./new"

def find_newest_c_or_cpp_file(directory):
    """Finds the newest .c or .cpp file in the specified directory."""
    newest_file = None
    newest_mtime = 0
    for filename in os.listdir(directory):
        if not filename.endswith(('.c', '.cpp')):
            continue
        filepath = os.path.join(directory, filename)
        mtime = os.path.getmtime(filepath)
        if mtime > newest_mtime:
            newest_file = filepath
            newest_mtime = mtime
    return newest_file

def extract_with_regex(file_path):
    """Extracts string and numerical literals from the file using regex."""
    regex_patterns = [
        r'"([^"\\]*(?:\\.[^"\\]*)*)"',  # String literals
        r'\b\d+\b'  # Numerical constants
    ]
    seeds = set()
    with open(file_path, 'r') as file:
        content = file.read()
        for pattern in regex_patterns:
            seeds.update(re.findall(pattern, content))
    return seeds

def extract_with_ast(file_path):
    """Extracts string literals from the file using the Clang AST."""
    index = Index.create()
    translation_unit = index.parse(file_path)
    seeds = set()
    for token in translation_unit.cursor.get_tokens():
        if token.kind == TokenKind.LITERAL and token.spelling.startswith('"'):
            seeds.add(token.spelling)
    return seeds

def generate_exploit_seeds():
    """Generates a set of seeds designed to test common vulnerabilities."""
    buffer_size = 50  # Example buffer size based on typical vulnerable buffer lengths
    return {
        "",  # Empty string
        "A" * (buffer_size - 1),  # Just below boundary
        "A" * buffer_size,  # At boundary
        "A" * (buffer_size + 1),  # Just over boundary
        "%s%p%x%d",  # Common format string exploits
        "AAAA" + "\x00" + "BBBB",  # Null byte injection
        ";\nls\n",  # Command injection
        "`id`",  # Command execution via backticks
        "admin\0"  # Null byte termination
    }

def save_seeds(seeds, output_file="./ongoing/seed/seeds.txt"):
    """Saves the generated seeds to a file."""
    with open(output_file, "w") as file:
        for seed in sorted(seeds):  # Sort seeds for easier review
            file.write(f"{seed}\n")
    print(f"Seeds saved to {output_file}")

def main():
    newest_file = find_newest_c_or_cpp_file(DIRECTORY)
    if newest_file:
        print(f"Analyzing the newest file: {newest_file}")
        regex_seeds = extract_with_regex(newest_file)
        ast_seeds = extract_with_ast(newest_file)
        exploit_seeds = generate_exploit_seeds()
        
        combined_seeds = regex_seeds.union(ast_seeds).union(exploit_seeds)
        
        save_seeds(combined_seeds)
    else:
        print("No .c or .cpp files found in the directory.")

if __name__ == "__main__":
    main()
