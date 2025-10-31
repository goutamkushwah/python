# Date - 31/10/2025
# WAP for  counting words in python.
# Reading from a file
with open("example.txt", "r") as file:
    text = file.read()

# Counting words
words = text.split()
print("Total number of words in file:", len(words))
