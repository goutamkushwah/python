f = open("File/file.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:
with open("File/file.txt") as f:
    print(f.read())

# You dont have to explicitly close the file