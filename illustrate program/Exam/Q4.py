# You need a Python program that: Displays a list of authors’ last names. Shows all titles each author has published.
# Results should be sorted by the author’s last name. Must use a JOIN (so we assume two tables: Authors and Books).
import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# SQL Query using LEFT JOIN (to include authors without books)
query = """
SELECT a.last_name, b.title
FROM Authors a
LEFT JOIN Books b ON a.author_id = b.author_id
ORDER BY a.last_name;
"""

cursor.execute(query)

# Display results
for row in cursor.fetchall():
    last_name, title = row
    print(f"Author: {last_name}, Book: {title}")

# Close connection
conn.close()