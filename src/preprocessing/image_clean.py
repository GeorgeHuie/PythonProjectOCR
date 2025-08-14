import cv2
import numpy as np
from PIL import Image

def to_grayscale(image: np.ndarray) -> np.ndarray:
    """convert image to grayscale"""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def threshold(image: np.ndarray) -> np.ndarray:
    _, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh

def remove_noise(image: np.ndarray) -> np.ndarray:
    kernal = np.ones((1, 1), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernal)

def deskew_image(image: np.ndarray) -> np.ndarray:
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    m = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, m, (w, h), flags = cv2.INTER_CUBIC, borderMode = cv2.BORDER_REPLICATE)

def load_image(path: str) -> np.ndarray:
    return cv2.imread(path)

def save_image(path: str, image: np.ndarray):
    cv2.imwrite(path, image)
