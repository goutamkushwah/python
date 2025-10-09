# Date 06-10-2025
# Write a program to mine a log file and find out whether it contains ‘python’. 
with open("Pratice-set/Chapter-9/Python.txt", "r") as f:
    content = f.read()
if "Python" in content:
    print("Yes, 'python' is present in the file")
else:
    print("No, 'python' is not present in the file")