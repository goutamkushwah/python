# r - read
# a - append
# w - write
# x - create
import os
f = open("new.txt", "r")
# print(f.read())
# print(f.read(4))
# print(f.readline())

# for line in f:
#     print(line, end="")
    
# f.close()    

# try:
#     f = open("new.txt", "r")
#     print(f.read())
# except Exception as e:
#     print("The file is does not exist")
# finally:
#     f.close()

# Append - creates the file if it doesn't exist
# f = open("a.txt", "a")
# f.write("This is a new line")
# f.close()

# f = open("new.txt")
# f.write("This is a new line")  # Error
# f.close()

# Creates the specified file , but returns an error
if not os.path.exists('a.txt'):
    f = open('a.txt','x') 
    f.close()