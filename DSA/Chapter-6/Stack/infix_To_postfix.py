def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []

    for char in expression:
        if char.isalnum():  # If the character is an operand (number/letter)
            output.append(char)
        elif char == '(':  # If the character is '(', push it to the stack
            stack.append(char)
        elif char == ')':  # If the character is ')', pop and output from the stack until an '(' is encountered
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop the '(' from the stack
        else:  # An operator is encountered
            while (stack and stack[-1] != '(' and
                   precedence[char] <= precedence[stack[-1]]):
                output.append(stack.pop())
            stack.append(char)

    # Pop all the operators from the stack
    while stack:
        output.append(stack.pop())

    return ''.join(output)

if __name__ == "__main__":
    expression = "A+B*(C^D-E)"
    print("Infix Expression: ", expression)
    print("Postfix Expression: ", infix_to_postfix(expression))