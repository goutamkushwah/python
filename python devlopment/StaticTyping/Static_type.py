name: str = "Goutam"
age: int = 21

def greet(name: str) -> str:
    return "Hello " + name

print(greet(name))

print(type(name))
print(type(age))