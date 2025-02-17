import fitz  # PyMuPDF

# Reload the new PDF file
pdf_path = r"" # add input file
doc = fitz.open(pdf_path)

# Extract text with positional data to locate "split" positions
page = doc[0]
text_instances = []

# Search for the word "split" in the text and record its positions
for inst in page.search_for("split"):
    text_instances.append(inst.y1)  # Capture the bottom y-coordinate of each "split" keyword

# Ensure the positions are sorted
text_instances.sort()

# Create a new PDF to store the split pages
new_doc = fitz.open()

# Split the page at each "split" marker
previous_y = 0
page_width = page.rect.width

for split_y in text_instances:
    rect = fitz.Rect(0, previous_y, page_width, split_y)
    new_page = new_doc.new_page(width=page_width, height=split_y - previous_y)
    new_page.show_pdf_page(new_page.rect, doc, 0, clip=rect)
    previous_y = split_y

# Handle any remaining portion after the last split marker
if previous_y < page.rect.height:
    rect = fitz.Rect(0, previous_y, page_width, page.rect.height)
    new_page = new_doc.new_page(width=page_width, height=page.rect.height - previous_y)
    new_page.show_pdf_page(new_page.rect, doc, 0, clip=rect)

# Save the split PDF
split_pdf_path = r"" # add output file
new_doc.save(split_pdf_path)
new_doc.close()

# Provide the download link
split_pdf_path
