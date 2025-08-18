import sqlite3
import re

def init_db(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS patient (
    name TEXT,
    dob TEXT,
    sex TEXT,
    UNIQUE(name, dob) --prevent duplicates
    )
    """
    )
    conn.commit()
    return conn

def parse_patient_info(text):
    name_match = re.search(r"Patient Demographics\s*\n([A-Za-z ]+)", text)
    dob_match = re.search(r"Date of Birth:\s*([0-9/]+)", text)
    sex_match = re.search(r"Sex:\s*([A-Za-z]+)", text)

    return {
        "name": name_match.group(1).strip() if name_match else "None",
        "dob": dob_match.group(1).strip() if dob_match else None,
        "sex": sex_match.group(1).strip() if sex_match else None,
    }

def save_patient_to_db(conn, patient):
    cur = conn.cursor()
    cur.execute("""
    INSERT OR IGNORE INTO patient (name, dob, sex)
    values (?, ?, ?)
    """,(patient["name"], patient["dob"], patient["sex"]))
    conn.commit()


