# from collections import deque
# queue = deque()
# queue.append("Task 1")
# queue.append("Task 2")
# queue.append("Task 3")
# print(queue)
# first_item = queue.popleft()
# print(f"Removed: {first_item}")
# print(f"Remaining: {list(queue)}")

from queue import Queue
q = Queue()
q.put("Data A")  # Enqueue
q.put("Data B")
print(q)
print(list(q.queue))
print(q.get()) 
print(q.get())
print(list(q.queue))


# from collections import deque

# class MyQueue:
#     def __init__(self):
#         self.container = deque()
        
#     def enqueue(self, val):
#         self.container.append(val)
        
#     def dequeue(self):
#         return self.container.popleft()
    
#     def __repr__(self):
#         return f"Queue({list(self.container)})"

# # Usage
# a = MyQueue()
# a.enqueue(1)
# a.enqueue(2)
# print(a) # Output: Queue([1, 2])
# a.dequeue()
# a.dequeue()