a = "This is a string"
print(a)
# get data type of variable
print(type(a))
# length of string
print(len(a))
# access characters by index
print(a[0])
# iterate all String
for i in a:
    print(i)
# access last iteam
print(a[-1])
# slicing
print(a[0:7])
print (a[4:])
print(a[:7])
print(a[0:10:2])
# String Methods
print(a.upper())
print(a.lower())
print(a.strip())

print(a.replace("is", "was"))
print(a.split(" "))
print("is" in a)
print("was" not in a)
print(a.find("string"))
print(a.index("string"))
print(a.count("is"))
print(a.startswith("This"))
print(a.endswith("string"))
print(a.capitalize())
print(a.title())
print(a.center(50, "-"))
print(a.encode())
print(a.format())
print(f"Formatted string: {a}")
print("Concatenated string: " + a)

# formatted string literals (f-strings)
name = "Goutam"
age = 23
print(f"My name is {name} and I am {age} years old.")