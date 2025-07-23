import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

print("\n✅ Cleaned users in database:")
for row in rows:
    print(row)

conn.close()
