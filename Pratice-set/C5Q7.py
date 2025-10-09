# Date 03-10-2025
# If the names of 2 friends are same; what will happen to the program in problem 
# 6? 
d = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ") # Same name as previous and value will be updated
lang = input("Enter Language name: ")
d.update({name: lang})

print(d)