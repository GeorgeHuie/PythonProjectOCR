import os
import cv2

#list all image files in given folder
def list_images(folder_path):
    return [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff"))
    ]

# create a folder with given path if not existed
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return  path