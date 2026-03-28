#WAP For File Handling(Create, Write, Read, Append and Copy File)in python

# 1️⃣ Create and Write to File
file = open("sample.txt", "w")   # 'w' creates file if not exists
file.write("first line.\n")
file.close()

print("File created and data written.\n")


# 2️⃣ Read File
file = open("sample.txt", "r")
content = file.read()
print("After Writing:")
print(content)
file.close()


# 3️⃣ Append to File
file = open("sample.txt", "a")
file.write("line appended later.\n")
file.close()

print("Data appended.\n")


# 4️⃣ Read Again After Append
file = open("sample.txt", "r")
print("After Appending:")
print(file.read())
file.close()


# 5️⃣ Copy File
source = open("sample.txt", "r")
destination = open("copy_sample.txt", "w")

destination.write(source.read())

source.close()
destination.close()

print("\nFile copied successfully as copy_sample.txt")