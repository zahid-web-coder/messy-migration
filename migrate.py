import sqlite3
import re

def clean_email(email):
    return email.lower().strip()

def clean_phone(phone):
    digits = re.sub(r'\D', '', phone)
    if len(digits) == 10:
        return f"+91-{digits}"
    elif len(digits) == 12 and digits.startswith("91"):
        return f"+{digits[:2]}-{digits[2:]}"
    else:
        return None


conn = sqlite3.connect('database.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT
    )
''')


cursor.execute('SELECT firs_t_name, lst_name, mail, phone_num FROM usres')
rows = cursor.fetchall()


for row in rows:
    first_name = row[0].strip().title()
    last_name = row[1].strip().title()
    email = clean_email(row[2])
    phone = clean_phone(row[3])

    try:
        cursor.execute('''
            INSERT INTO users (first_name, last_name, email, phone)
            VALUES (?, ?, ?, ?)
        ''', (first_name, last_name, email, phone))
    except sqlite3.IntegrityError:
        print(f"Skipping duplicate or invalid email: {email}")

conn.commit()


print("✅ Data cleaned and migrated successfully.")
print("\n✅ Migrated rows in 'users' table:")
cursor.execute('SELECT * FROM users')
for row in cursor.fetchall():
    print(row)

conn.close()
