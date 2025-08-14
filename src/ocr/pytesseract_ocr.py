import pytesseract
from PIL import Image
import numpy as np

def pytesseract_ocr(image_input):
    if isinstance(image_input, str):
        img = Image.open(image_input)
    elif isinstance(image_input, np.ndarray):
        img = Image.fromarray(image_input)
    else:
        raise TypeError("Input must be str or np.ndarray")
    return pytesseract.image_to_string(img)