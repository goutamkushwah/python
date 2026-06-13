# Basic Inference
from typing import reveal_type

answer = 42
reveal_type(answer) # hover to reveal type

fruits = ["apple", "banana", "cherry"]
scores = {"math": 95, "science": 90}

def greet(name):
  return f"Hello, {name}!"

message = greet("World")
reveal_type(message) # hover to reveal type