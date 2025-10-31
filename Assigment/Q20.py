# Date - 31/10/2025
# WAP for copy files in python.
# Method 1: Using File Handling

# Get source and destination file names
source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

# Open and copy content
with open(source_file, "r") as src:
    content = src.read()

with open(destination_file, "w") as dest:
    dest.write(content)

print(f"File '{source_file}' has been copied to '{destination_file}' successfully.")
