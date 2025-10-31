# Date 31/10/2025
#  WAP for reading & writing files in python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("Python makes file handling easy!\n")

print("Data written to file successfully.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("\nReading data from file:")
    print(content)
