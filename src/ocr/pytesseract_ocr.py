import pytesseract
from PIL import Image
import numpy as np

#perform OCR using pytesseract
def pytesseract_ocr(image_input):
    if isinstance(image_input, str): #check str file path
        img = Image.open(image_input) #open image using PIL
    elif isinstance(image_input, np.ndarray): #check np array path
        img = Image.fromarray(image_input) #conver array to PIL image
    else:
        raise TypeError("Input must be str or np.ndarray") #raise error if the file is neither np array or str
    return pytesseract.image_to_string(img) #extract string