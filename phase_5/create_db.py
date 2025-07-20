import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('site.db')
cursor = conn.cursor()

# Create a table for users
cursor.execute('''
CREATE TABLE users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               email TEXT UNIQUE NOT NULL
               )
''')

conn.commit()
conn.close()