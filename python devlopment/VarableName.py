language: str = "Python"
number: int = 42
coefficient: float = 2.87
print(f"Language: {language}, Number: {number}, Coefficient: {coefficient}")

# parrlel Assigment
is_authenticated = is_active = is_admin = False
print(is_authenticated)
print(is_active)
print(is_admin)

i=j=0
for i in range(3):
    j += i

# iterable Unpacking
a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)

prrson = ("Alice", 30, "Engineer")
name, age, profession = prrson
print(name)
print(age)
print(profession)



# Assignment Expressions
line = input("Type some text: ")
while line != "stop":
     print(line)
     line = input("Type some text: ")


# Deltting Variables from their scopre
x = 10
print(x)
del x
# print(x)  # This will raise a NameError since x has been deleted