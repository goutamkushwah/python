marks = {
    "Goutam": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Goutam"
}

# Printing dictionary data
print(marks.items())    # Prints all key-value pairs
print(marks.keys())     # Prints all keys
print(marks.values())   # Prints all values

# Updating dictionary
marks.update({"Goutam": 99, "Renuka": 100})
print(marks)

# Safe access with .get()
print(marks.get("Goutam2", "Key Not Found"))   # Prints "Key Not Found"
print(marks.get("Goutam", "Key Not Found"))    # Prints 99
