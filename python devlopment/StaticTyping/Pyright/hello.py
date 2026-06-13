def greet(name: str) -> str:
    return "Hello, " + name

greet("World")  # ✅ OK
# pyrefly: ignore [bad-argument-type]
greet(42)       # ❌ Type error
# print('hello)