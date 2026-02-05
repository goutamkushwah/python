from collections import deque
stack= deque([])
stack.appendleft(10)
stack.appendleft(20)
print(stack)
stack.appendleft(30)
print(stack)
stack.popleft()
print(stack)