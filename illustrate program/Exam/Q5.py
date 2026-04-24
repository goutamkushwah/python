import sqlite3
import tkinter as tk
from tkinter import messagebox

# Create in-memory database
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# Function to insert data
def add_student():
    name = entry_name.get()
    age = entry_age.get()

    if name == "" or age == "":
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    messagebox.showinfo("Success", "Student added successfully")

# Function to display data
def show_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    text_output.delete("1.0", tk.END)
    for row in records:
        text_output.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}\n")


# GUI Window
root = tk.Tk()
root.title("Student Information System")

# Labels & Entries
tk.Label(root, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Age").grid(row=1, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1)

# Buttons
tk.Button(root, text="Add Student", command=add_student).grid(row=2, column=0)
tk.Button(root, text="Show Students", command=show_students).grid(row=2, column=1)

# Output box
text_output = tk.Text(root, height=10, width=40)
text_output.grid(row=3, column=0, columnspan=2)

# Run GUI
root.mainloop()