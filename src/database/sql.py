import sqlite3
import re

# connect to a db file and create a patient table if it doesn't exist
def init_db(db_path):
    conn = sqlite3.connect(db_path) #connect to the db file
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS patient (
    name TEXT,
    dob TEXT,
    sex TEXT,
    UNIQUE(name, dob) --prevent duplicates
    )
    """
    ) #create a table if there is no such table
    conn.commit()
    return conn

#go through the text from the OCR and search for distinct patient info
def parse_patient_info(text):
    name_match = re.search(r"Patient Demographics\s*\n([A-Za-z ]+)", text) #search for a name
    dob_match = re.search(r"Date of Birth:\s*([0-9/]+)", text) # search for the dob
    sex_match = re.search(r"Sex:\s*([A-Za-z]+)", text) #search for gender

    #return a dictionary include name, dob, and gender
    return {
        "name": name_match.group(1).strip() if name_match else "None",
        "dob": dob_match.group(1).strip() if dob_match else None,
        "sex": sex_match.group(1).strip() if sex_match else None,
    }

#save the information into the patient table
def save_patient_to_db(conn, patient):
    cur = conn.cursor()
    cur.execute("""
    INSERT OR IGNORE INTO patient (name, dob, sex)
    values (?, ?, ?)
    """,(patient["name"], patient["dob"], patient["sex"])) #insert info if it is unique
    conn.commit()


