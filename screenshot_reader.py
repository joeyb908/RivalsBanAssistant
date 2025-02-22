import easyocr
import glob
import os

FILE_DIRECTORY = glob.glob('./screenshots/*') # * means all if need specific format then *.csv
IMAGE_PATH = max(FILE_DIRECTORY, key=os.path.getmtime)
reader = easyocr.Reader(['en'], download_enabled=False, model_storage_directory="./models")

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

def read_profile_names():
    text = reader.readtext(IMAGE_PATH)
    profile_names = []

    for word in text:
        profile_name = word[1].split()
        if len(profile_name) > 1:
            if len(profile_name[1]) > 2:
                profile_names.append(profile_name[1])

    return profile_names