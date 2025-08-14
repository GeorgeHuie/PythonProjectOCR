import os
import cv2

def list_images(folder_path):
    return [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff"))
    ]

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return  path