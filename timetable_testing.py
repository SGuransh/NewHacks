import re
from pdfminer.high_level import extract_pages, extract_text

# for page_layout in extract_pages("timetable.pdf"):
#     for element in page_layout:
#         print(element)


text = extract_text("timetable.pdf")
print(text.split("\n"))
