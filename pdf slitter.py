# splitter.py

from PyPDF2 import PdfReader, PdfWriter
import os

def split_pdf(file_path, output_dir):
    reader = PdfReader(file_path)
    total_pages = len(reader.pages)

    for i in range(total_pages):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])
        output_filename = os.path.join(output_dir, f'page_{i+1}.pdf')
        with open(output_filename, 'wb') as f:
            writer.write(f)
        print(f"✅ Saved: {output_filename}")

def split_pdf_range(file_path, output_dir, page_ranges):
    reader = PdfReader(file_path)

    for idx, (start, end) in enumerate(page_ranges, start=1):
        writer = PdfWriter()
        for page_num in range(start-1, end):
            writer.add_page(reader.pages[page_num])
        output_filename = os.path.join(output_dir, f'range_{idx}_{start}-{end}.pdf')
        with open(output_filename, 'wb') as f:
            writer.write(f)
        print(f"✅ Saved: {output_filename}")

if __name__ == "__main__":
    input_pdf = "input/sample.pdf"
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    print("🔹 Splitting all pages individually...")
    split_pdf(input_pdf, output_folder)

    print("\n🔹 Splitting by page ranges (1–3, 4–5)...")
    split_pdf_range(input_pdf, output_folder, [(1, 3), (4, 5)])

