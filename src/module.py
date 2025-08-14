# modules.py — Auto-import all functions & classes from src submodules

# modules.py

# Import all preprocessing functions
from preprocessing.image_clean import (
    load_image,
    save_image,
    to_grayscale,
    threshold,
    remove_noise,
    deskew_image
)

# Import OCR wrapper
from ocr.pytesseract_ocr import pytesseract_ocr

# Import utils
from utils.file_ops import list_images, create_folder

# Optionally define __all__ for cleaner namespace
__all__ = [
    'load_image',
    'save_image',
    'to_grayscale',
    'threshold',
    'remove_noise',
    'deskew_image',
    'pytesseract_ocr',
    'list_images',
    'create_folder'
]
