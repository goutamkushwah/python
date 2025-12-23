Stack = []
max_size = 100

def push(element):
    if len(Stack) < max_size:
        Stack.append(element)
        print(f"Pushed {element} to stack")
    else:
        print("Stack Overflow")

# # pop operation

def pop():
    if len(Stack) == 0:
        print("Stack Underflow")
    else:
        item = Stack.pop()
        print("Popped item:", item)
def size():
    return len(Stack)

def peek():
    if len(Stack) == 0:
        print("Stack is empty")
    else:
        return Stack[-1]

def is_empty():
    if len(Stack) == 0:
        return True
    else:
        return False
    

push(10)
push(20)
push(30)

print("Top element:", peek())
print("Size:", size())

pop()

print("Is empty?", is_empty())
print("Stack:", Stack)
