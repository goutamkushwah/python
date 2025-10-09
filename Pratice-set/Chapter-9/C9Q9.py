# Date 06-10-2025
# Write a program to find out whether a file is identical & matches the content of 
# another file. 
with open("Pratice-set/Chapter-9/copy.txt", "r") as f:
    content1 = f.read()
with open("Pratice-set/Chapter-9/this.txt", "r") as f:
    content2 = f.read()
if content1 == content2:
    print("The files are identical.")
else:
    print("The files are not identical.")        
