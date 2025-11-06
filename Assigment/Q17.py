# Date - 31/10/2025
# WAP for implementing packages in python
# Importing functions from package
from arithmetic import add, sub

def main():
    x = 15
    y = 10
    print("Addition:", add(x, y))
    print("Subtraction:", sub(x, y))

if __name__ == "__main__":
    main()


#  folder structure:

# Assigment/
# │
# ├── __init__.py
# ├── arithmetic/
# │   ├── __init__.py
# │   ├── add.py
# │   └── sub.py
# └── main.py
