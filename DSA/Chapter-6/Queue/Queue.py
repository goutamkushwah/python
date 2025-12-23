queue= []
Max=10
# Enqueue
def Enqueue(item):
    if len(queue) < Max:
        queue.append(item)
        print(f"Enqueued {item} to queue")
    else:
        print("Queue Overflow")
# dequeue
def Dequeue():
    if len(queue)==0:
        print("Queue Underflow")
    else:
        queue.pop(0)
        print("Dequeued item")
def size():
    return len(queue)
def front():
    if len(queue)==0:
        print("Queue is empty")
    else:
        return queue[0]
def rear():
    if len(queue)==0:
        print("Queue is empty")
    else:
        return queue[-1]
def is_empty():
    if len(queue)==0:
        return True
    else:
        return False
def is_full():
    if len(queue)==Max:
        return True
    else:
        return False
Enqueue(10)
Enqueue(20)
Enqueue(30)
print("Front element:", front())
print("Rear element:", rear())
print("Size:", size())
Dequeue()
print("Is empty?", is_empty())
print("Is full?", is_full())
print("Queue:", queue)
                 