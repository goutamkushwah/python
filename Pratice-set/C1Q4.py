# Date 03-10-2025
# . Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that.  
import os

def list_directory_contents(path='.'):
    """
    Print the names of entries in the directory given by `path`.
    Defaults to current directory if no path is given.
    """
    try:
        entries = os.listdir(path)  # returns list of names (files + dirs) :contentReference[oaicite:1]{index=1}
    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found.")
        return
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
        return
    except OSError as e:
        print(f"Error reading directory '{path}': {e}")
        return

    print(f"Contents of directory '{path}':")
    for name in entries:
        print(name)


if __name__ == "__main__":
    # you can change '.' to any directory path you want
    list_directory_contents('.')
