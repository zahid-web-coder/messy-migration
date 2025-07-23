import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS usres (
        firs_t_name TEXT,
        lst_name TEXT,
        mail TEXT,
        phone_num TEXT
    )
''')


cursor.execute("INSERT INTO usres VALUES ('John', 'Doe', 'john@example.com', '1234567890')")
cursor.execute("INSERT INTO usres VALUES ('Jane', 'Smith', 'jane@example.com', '9876543210')")
cursor.execute("INSERT INTO usres VALUES ('Bob', 'Johnson', 'bob@example.com', '5555555555')")

conn.commit()
conn.close()

print("Database initialized with sample data")
