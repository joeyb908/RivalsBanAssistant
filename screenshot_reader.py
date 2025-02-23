from numpy import array
import pytesseract
from cv2 import imread, cvtColor, COLOR_BGR2GRAY
import glob
import os

FILE_DIRECTORY = glob.glob(os.environ["IMAGES_DIRECTORY"])# * means all if need specific format then *.csv
IMAGE_PATH = max(FILE_DIRECTORY, key=os.path.getmtime)

def image_to_string():
    names = []

    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = os.environ["TESSERACT_EXE"]

    # Capture image
    # Convert the image to monochrome for it to be easily
    # read by the OCR and obtained the output String.
    cap = imread(IMAGE_PATH)
    gray = cvtColor(array(cap), COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, lang='eng')

    # Parse through text anda
    for words in text.splitlines():
        if len(words) > 0:
            names.append(words)

    return names