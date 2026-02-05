from collections import deque
queue= deque([])
queue.append(10)
queue.append(20)
print(queue)
queue.append(30)
print(queue)
queue.popleft()
print(queue)