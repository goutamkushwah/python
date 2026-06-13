def greet(name: str) -> str:
    return "Hello, " + name

message = greet("World")  # ✅ OK

# error_message = greet(42)  # ❌ Type Error