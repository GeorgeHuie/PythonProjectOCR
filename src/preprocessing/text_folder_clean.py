import os
import re


#extract the name of patient base on searching for the first line
def extract_name(text):
    first_line = text.strip().split('\n')[0].strip()
    #search for the name with pattern
    name_match = re.search(r'[A-Z][a-z]+', first_line)
    if name_match:
        return name_match.group(0)
    else:
        return "Unknown Patient"

#save the text extracted from OCR to a file with the patient's name
def save_text_to_file(text, folder):
    patient_name = extract_name(text)
    safe_name = patient_name.replace(" ", "_")
    filename = os.path.join(folder, safe_name)
    with open(filename, 'w', encoding= 'utf-8') as f:
        f.write(text)
    print("saved text file to {}".format(filename))
