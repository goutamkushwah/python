# Write a Python program that: Counts the total number of spaces in a file. Counts the total number of characters in a file.
# Counts the total number of lines in a file.


# Open the file in read mode
file = open("sample.txt", "r")

spaces = 0
characters = 0
lines = 0

for line in file:
    lines += 1
    characters += len(line)   # counts all characters including spaces & newline
    spaces += line.count(" ")  # counts only space characters

file.close()

print("Total Lines:", lines)
print("Total Characters:", characters)
print("Total Spaces:", spaces)