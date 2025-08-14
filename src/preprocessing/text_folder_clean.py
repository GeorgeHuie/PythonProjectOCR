import os
import re

def extract_name(text):
    first_line = text.strip().split('\n')[0].strip()
    name_match = re.search(r'[A-Z][a-z]+', first_line)
    if name_match:
        return name_match.group(0)
    else:
        return "Unknown Patient"

def save_text_to_file(text, folder):
    patient_name = extract_name(text)
    safe_name = patient_name.replace(" ", "_")
    filename = os.path.join(folder, safe_name)
    with open(filename, 'w', encoding= 'utf-8') as f:
        f.write(text)
    print("saved text file to {}".format(filename))
