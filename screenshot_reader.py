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

    # Capture, convert to monochrome, and read OCR
    cap = imread(IMAGE_PATH)
    gray = cvtColor(array(cap), COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, lang='eng')

    # Parse through text and assign list if characters exist
    names = [words for words in text.splitlines() if words]

    return names