import cv2
import numpy as np
from PIL import Image

#conver colored image to grayscale
def to_grayscale(image: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#apply
def threshold(image: np.ndarray) -> np.ndarray:
    _, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh

#remove small noise using morphological opening
def remove_noise(image: np.ndarray) -> np.ndarray:
    kernal = np.ones((1, 1), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernal)

#correct skew on the image to align text horizontally
def deskew_image(image: np.ndarray) -> np.ndarray:
    #find coordinate of the character pixel
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    #adjust angle to ensure proper rotation direction
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    #find the center
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    #compute rotation matrix
    m = cv2.getRotationMatrix2D(center, angle, 1.0)
    # apply transformation
    return cv2.warpAffine(image, m, (w, h), flags = cv2.INTER_CUBIC, borderMode = cv2.BORDER_REPLICATE)

#loaf image from a given file path
def load_image(path: str) -> np.ndarray:
    return cv2.imread(path)

#store image in given a file path
def save_image(path: str, image: np.ndarray):
    cv2.imwrite(path, image)
