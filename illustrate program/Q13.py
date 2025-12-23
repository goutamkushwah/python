# Date - 23/11/2025
# WAP to count number of words in a text file

import os

path = r"D:\python\cource\illustrate program\text.txt"  # use raw string for Windows path

try:
    with open(path, "r", encoding="utf-8") as f:
        word_count = sum(len(line.split()) for line in f)
    print("Word count =", word_count)
except FileNotFoundError:
    print(f"Error: file not found: {os.path.abspath(path)}")
except UnicodeDecodeError:
    print("Error: could not decode file. Try a different encoding (e.g. 'latin-1').")