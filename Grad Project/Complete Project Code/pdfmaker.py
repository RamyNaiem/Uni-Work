from fpdf import FPDF
from datetime import date
from pathlib import Path
import difflib

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Code Healer Report', 0, 1, 'L')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def calculate_similarity(text1, text2):
    if text1 and text2:  # Only calculate similarity if both texts are available
        return difflib.SequenceMatcher(None, text1, text2).ratio()
    return 0

# Setup file paths and read files
finished_dir = Path('/home/ramy/Desktop/folda/Finished')
newest_folder = max(finished_dir.iterdir(), key=lambda x: x.stat().st_mtime if x.is_dir() else float('-inf'))
crashes_dir = newest_folder / 'output' / 'default' / 'crashes'
newest_file = max(crashes_dir.iterdir(), key=lambda x: x.stat().st_mtime if x.is_file() else float('-inf'))

crash_content = ''
response_gpt = ''
response_gemini = ''

if newest_file.exists():
    with open(newest_file, 'r') as file:
        crash_content = file.read()

chat_response_path = newest_folder / 'chatgpt_response.txt'
ai_response_path = newest_folder / 'Ai_response.txt'

if chat_response_path.exists():
    with open(chat_response_path, 'r') as file:
        response_gpt = file.read()

if ai_response_path.exists():
    with open(ai_response_path, 'r') as file:
        response_gemini = file.read()

# Calculate similarity
similarity_score = calculate_similarity(response_gpt, response_gemini)
similarity_desc = f"Similarity score: {similarity_score:.2f}/1.00"

# Create PDF
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, 'CODE HEALER', 0, 1, 'L')
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, str(date.today()), 0, 1, 'L')
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, "Crash reason:", 0, 1)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, crash_content)
if response_gpt:
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, 'ChatGPT Solution:', 0, 1)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f'{similarity_desc}\n{response_gpt}')
if response_gemini:
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, 'Gemini Solution:', 0, 1)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f'{similarity_desc}\n{response_gemini}')

# Save the PDF
pdf_output_path = newest_folder / 'CODE_HEALER.pdf'
pdf.output(str(pdf_output_path))
print(f"PDF saved to {pdf_output_path}")
