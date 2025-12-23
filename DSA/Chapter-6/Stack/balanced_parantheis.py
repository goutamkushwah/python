
def is_balanced(expression):
    stack = []
    # Mapping closing brackets to their opening counterparts
    mapping = {")": "(", "}": "{", "]": "["}

    for char in expression:
        if char in mapping.values():  # If it's an opening bracket
            stack.append(char)
        elif char in mapping:         # If it's a closing bracket
            if not stack or stack.pop() != mapping[char]:
                return False
    
    return len(stack) == 0

# Testing
print(is_balanced("{[()]}")) # Output: True
print(is_balanced("{[(])}")) # Output: False