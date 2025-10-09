# Date 06-10-2025
# Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 
f= open("Pratice-set/Chapter-9/poem.txt","r")
data = f.read()
if "twinkle" in data:
    print("Yes, 'twinkle' is present in the file")
else:
    print("No, 'twinkle' is not present in the file")
f.close()    