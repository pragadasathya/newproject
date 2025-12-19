import sqlite3

conn = sqlite3.connect("booking.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    date TEXT,
    slot TEXT
)
""")

conn.commit()
conn.close()
print("Database initialized")
