# PDF Splitter by Keyword 📄✂️

A Python script that **automatically splits a PDF** based on occurrences of the keyword **"split"** within the document. It scans for the keyword’s position on a page and divides the content into separate sections accordingly.

## 🚀 Features
- 📌 **Keyword-Based Splitting**: Detects the keyword **"split"** and divides the page at those locations.  
- 📄 **Preserves Original Layout**: Ensures text and formatting remain intact.  
- 🔍 **Automatic Detection**: Uses **PyMuPDF (fitz)** to scan and process PDFs efficiently.  
- 💾 **Custom Output**: Saves the newly split sections as a separate PDF.  

## 🛠️ Installation
1. Install dependencies:
   ```bash
   pip install pymupdf
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/davidrencse/PDF-Splitter.git
   cd PDF-Splitter
   ```

## ▶️ Usage
1. Modify the script to set the correct PDF file path:
   ```python
   pdf_path = r"C:\path\to\your\file.pdf"
   ```
2. Run the script:
   ```bash
   python split_pdf.py
   ```
3. The output file will be saved in the same directory.

## 📜 Requirements
- **Python 3.x**
- **PyMuPDF (fitz)**

## 📌 Notes
- Ensure the PDF contains **searchable text** for the script to detect the keyword.  
- If your PDF is scanned (image-based), consider using **OCR tools** like `pytesseract` to extract text before running the script.

## 📜 License
MIT License  
