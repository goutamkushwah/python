# WAP for SQL Statements(Create a table, Insert records, Update records, Delete records) in python

# -------------------------------------
# WAP FOR SQL STATEMENTS
# (CREATE, INSERT, UPDATE, DELETE)
# -------------------------------------

import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("student.db")

# Create cursor object
cursor = conn.cursor()


# 1️⃣ CREATE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

print("Table created successfully.")


# 2️⃣ INSERT RECORDS
cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
               ("Goutam", 21, "BCA"))

cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
               ("Rahul", 22, "BSc"))

conn.commit()
print("Records inserted successfully.")


# 3️⃣ UPDATE RECORD
cursor.execute("UPDATE students SET age = ? WHERE name = ?",
               (23, "Goutam"))

conn.commit()
print("Record updated successfully.")


# 4️⃣ DELETE RECORD
cursor.execute("DELETE FROM students WHERE name = ?",
               ("Rahul",))

conn.commit()
print("Record deleted successfully.")


# 5️⃣ DISPLAY RECORDS
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("\nCurrent Records:")
for row in rows:
    print(row)


# Close connection
conn.close()