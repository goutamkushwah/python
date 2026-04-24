import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create Authors table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Authors (
    author_id INTEGER PRIMARY KEY,
    last_name TEXT
);
""")

# Create Books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    author_id INTEGER,
    FOREIGN KEY(author_id) REFERENCES Authors(author_id)
);
""")

# Insert sample data
cursor.execute("INSERT INTO Authors (author_id, last_name) VALUES (1, 'Sharma')")
cursor.execute("INSERT INTO Authors (author_id, last_name) VALUES (2, 'Verma')")

cursor.execute("INSERT INTO Books (title, author_id) VALUES ('Python Basics', 1)")
cursor.execute("INSERT INTO Books (title, author_id) VALUES ('Data Science', 1)")

conn.commit()
conn.close()