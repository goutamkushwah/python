# Date - 23/11/2025
# # WAP to count number of words in a text file
file = open("D:\python\cource\illustrate_program\text.txt", "r")
data = file.read()

words = data.split()
print("Word count =", len(words))

file.close()
