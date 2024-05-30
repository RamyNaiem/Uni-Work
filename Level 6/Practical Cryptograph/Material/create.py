import sqlite3

conn = sqlite3.connect('database.db')  # Make sure to use your actual database file
cursor = conn.cursor()

cursor.execute("ALTER TABLE users ADD COLUMN private_key BLOB")
cursor.execute("ALTER TABLE users ADD COLUMN public_key BLOB")

conn.commit()
conn.close()

