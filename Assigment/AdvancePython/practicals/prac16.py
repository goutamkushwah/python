# WAP for Components Handling in AP.

# -------------------------------------
# WAP FOR COMPONENTS HANDLING IN PYTHON
# -------------------------------------

import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Components Handling Example")
root.geometry("400x300")


# Function to handle button click
def process_data():
    name = entry_name.get()
    age = entry_age.get()

    # Update label dynamically
    result_label.config(text=f"Hello {name}, you are {age} years old.")

    # Insert into text box
    text_box.insert(tk.END, f"Name: {name}, Age: {age}\n")

    # Clear input fields
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)


# Labels
tk.Label(root, text="Enter Name:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

tk.Label(root, text="Enter Age:").pack(pady=5)
entry_age = tk.Entry(root)
entry_age.pack(pady=5)


# Button
submit_btn = tk.Button(root, text="Submit", command=process_data)
submit_btn.pack(pady=10)


# Result Label
result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=5)


# Text Box
text_box = tk.Text(root, height=5, width=40)
text_box.pack(pady=5)


# Run application
root.mainloop()