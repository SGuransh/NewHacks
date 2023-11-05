# import pytesseract
# from PIL import Image
# pytesseract.pytesseract.tesseract_cmd='/opt/homebrew/bin/tesseract'
#
#
# # Open the image using PIL (Pillow)
# image = Image.open('IMG_6477.jpg')
#
# # Use pytesseract to extract text from the image
# text = pytesseract.image_to_string('IMG_6477.jpg')
#
# # Print the extracted text
# print(text)
#


from pdfminer.high_level import extract_pages, extract_text

# for page_layout in extract_pages("timetable.pdf"):
#     for element in page_layout:
#         print(element)


text = extract_text("IMG_6477.pdf")

print(text)
