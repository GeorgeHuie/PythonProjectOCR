from module import (
    list_images, create_folder,
    load_image, save_image,
    to_grayscale, threshold, remove_noise, deskew_image,
    pytesseract_ocr,
)
import os
from preprocessing.text_folder_clean import save_text_to_file

if __name__ == '__main__':
    raw_folder = r"C:\Users\huieg\PycharmProjects\PythonProject\data\raw"

    processed_folder = r"C:\Users\huieg\PycharmProjects\PythonProject\data\processed"
    create_folder(processed_folder)

    image_paths = list_images(raw_folder)
    for img_path in image_paths:
        print(f"Processing {img_path}")

        img = load_image(img_path)
        gray = to_grayscale(img)
        binary = threshold(gray)
        clean = remove_noise(binary)
        deskew = deskew_image(clean)

        filename = os.path.basename(img_path)
        save_path = os.path.join(processed_folder, filename)
        save_image(save_path,deskew)

        text = pytesseract_ocr(deskew)
        save_text_to_file(text, save_path)
        print("ocr result:")
        print(text)
        print("-" * 50)
