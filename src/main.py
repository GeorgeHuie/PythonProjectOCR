from database.sql import parse_patient_info, save_patient_to_db, init_db
from module import (
    list_images, create_folder,
    load_image, save_image,
    to_grayscale, threshold, remove_noise, deskew_image,
    pytesseract_ocr,
)
import os
from preprocessing.text_folder_clean import save_text_to_file

#execute for extract text from a image and store the information into a database
if __name__ == '__main__':
    #raw image folder
    raw_folder = r"C:\Users\huieg\PycharmProjects\PythonProject\data\raw"

    #cleaned image folder
    processed_folder = r"C:\Users\huieg\PycharmProjects\PythonProject\data\processed"
    create_folder(processed_folder)

    #database folder and initialization
    database_folder = r"C:\Users\huieg\PycharmProjects\PythonProject\patients.db"
    create_folder(database_folder)
    conn = init_db(database_folder)

    #create a list of image path
    image_paths = list_images(raw_folder)

    #loop through the list to clean,
    for img_path in image_paths:
        print(f"Processing {img_path}")

        #clean image
        img = load_image(img_path)
        gray = to_grayscale(img)
        binary = threshold(gray)
        clean = remove_noise(binary)
        deskew = deskew_image(clean)

        #save clean image
        filename = os.path.basename(img_path)
        save_path = os.path.join(processed_folder, filename)
        save_image(save_path,deskew)

        #save extract text
        text = pytesseract_ocr(deskew)
        save_text_to_file(text, processed_folder)

        #store in a database file
        patient = parse_patient_info(text)
        save_patient_to_db(conn, patient)
