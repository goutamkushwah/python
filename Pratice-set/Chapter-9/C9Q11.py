# Date 06-10-2025
# Write a python program to rename a file to “renamed_by_ python.txt.
with open("Pratice-set/Chapter-9/old.txt", "r") as f:
    content = f.read()
with open("Pratice-set/Chapter-9/renamed_by_python.txt", "w") as f:
    f.write(content)    
# import os
# os.remove("Pratice-set/Chapter-9/old.txt")  # Removing the old file    

# this is dengourus if the file is large it will take time to copy and then delete the old file