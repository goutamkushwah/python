source = input("Enter source file name: ")     # example: a.txt
destination = input("Enter destination file: ")  # example: b.txt

f1 = open(source, "r")
f2 = open(destination, "w")

for line in f1:
    f2.write(line)

f1.close()
f2.close()

print("File copied successfully!")
