# Date 06-10-2025
# Write a program to make a copy of a text file “this. txt”
with open("Pratice-set/Chapter-9/copy.txt", "r") as f:
    content = f.read()
with open("Pratice-set/Chapter-9/this.txt", "w") as f:    
    f.write(content)