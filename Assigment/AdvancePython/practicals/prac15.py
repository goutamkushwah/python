#WAP for Event Handling in AP.

# -------------------------------------
# SIMPLE 2-FIELD FORM USING TKINTER
# -------------------------------------

import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Simple Form")
root.geometry("300x200")


# Function to handle submit event
def submit_form():
    name = entry_name.get()
    email = entry_email.get()

    if name == "" or email == "":
        messagebox.showerror("Error", "All fields are required!")
    else:
        messagebox.showinfo("Success", f"Name: {name}\nEmail: {email}")


# Labels
label_name = tk.Label(root, text="Name:")
label_name.pack(pady=5)

entry_name = tk.Entry(root)
entry_name.pack(pady=5)

label_email = tk.Label(root, text="Email:")
label_email.pack(pady=5)

entry_email = tk.Entry(root)
entry_email.pack(pady=5)


# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=10)


# Run application
root.mainloop()