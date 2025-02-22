import easyocr
import openocr
import glob
import os

FILE_DIRECTORY = glob.glob('./screenshots/*') # * means all if need specific format then *.csv
IMAGE_PATH = max(FILE_DIRECTORY, key=os.path.getmtime)
engine = openocr.OCR()
# reader = easyocr.Reader(['en'], download_enabled=False, model_storage_directory="./models")

#
# # Defining paths to tesseract.exe
# # and the image we would be using
# path_to_tesseract = r'/usr/local/bin/tesseract'
#
# Opening the image & storing it in an image object
# img = Image.open(IMAGE_PATH)
#
# # Providing the tesseract executable
# # location to pytesseract library
# # pytesseract.tesseract_cmd = path_to_tesseract
#
# # Passing the image object to image_to_string() function
# # This function will extract the text from the image
# text = pytesseract.image_to_string(img)

# Displaying the extracted text

# for word in text.split():
#     try:
#         val = int(word)
#     except ValueError:
#         profile_name = word
#         print(profile_name)

# def read_profile_names_easyocr():
#     text = reader.readtext(IMAGE_PATH)
#     profile_names = []
#
#     for word in text:
#         profile_name = word[1].split()
#         print(profile_name)
#         for name in profile_name:
#             print(name)
#             try:
#                 val = int(name)
#             except ValueError:
#                 if len(name) > 2:
#                     try:
#                         val = int(name[:1])
#                         name = name[2:]
#
#                     except ValueError:
#                         pass
#
#                     if name[0] == "1":
#                         name = name[1:]
#
#                     name = name.replace(':', '.')
#                     profile_names.append(name)
#
#     return profile_names

def read_profile_names_openocr():
    result, elapse = engine(IMAGE_PATH)
    print(result)