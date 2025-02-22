import numpy as nm
import pytesseract
import cv2
import glob
import os

FILE_DIRECTORY = glob.glob('C:/Users/joeyb/OneDrive/Documents/ShareX/Screenshots/2025-02/*') # * means all if need specific format then *.csv
IMAGE_PATH = max(FILE_DIRECTORY, key=os.path.getmtime)
# reader = easyocr.Reader(['en'], download_enabled=False, model_storage_directory="./models")

def imToString():
    names = []
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    # ImageGrab-To capture the screen image in a loop.
    # Bbox used to capture a specific area.
    cap = cv2.imread(IMAGE_PATH)
    gray = cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY)

    # Converted the image to monochrome for it to be easily
    # read by the OCR and obtained the output String.
    text = pytesseract.image_to_string(gray, lang='eng')
    # print(text)
    for words in text.splitlines():
        # print(words)
        if len(words) < 4:
            continue
        words = words[3:]
        words = words.replace('\\', '')
        if words[0] == ' ':
            words = words[1:]
        if len(words) > 3:
            # print(words)
            names.append(words)

    return names

    # tesstr = pytesseract.image_to_string(
    #     cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
    #     lang='eng')

    # Calling the function


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