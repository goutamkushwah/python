# Date 31/10/2025
# WAP for command line argument in python. 
import sys

# sys.argv is a list that stores command-line arguments
print("Number of arguments:", len(sys.argv))
print("Arguments List:", sys.argv)

# Accessing individual arguments
if len(sys.argv) > 2:
    name = sys.argv[1]
    age = sys.argv[2]
    print(f"Hello {name}, you are {age} years old.")
else:
    print("Please provide your name and age as command-line arguments.")
