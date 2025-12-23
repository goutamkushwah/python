Circular_queue=[]
def Enqueue(item):
    Circular_queue.append(item)
    print(f"Enqueued {item} to circular queue")
def Dequeue():
    if len(Circular_queue)==0:
        print("Circular Queue Underflow")
    else:
        item = Circular_queue.pop(0)
        Circular_queue.append(item)
        print("Dequeued item:", item)
def size():
    return len(Circular_queue)
def front():
    if len(Circular_queue)==0:
        print("Circular Queue is empty")
    else:
        return Circular_queue[0]
def rear():
    if len(Circular_queue)==0:
        print("Circular Queue is empty")
    else:
        return Circular_queue[-1]
def is_empty():
    if len(Circular_queue)==0:
        return True
    else:
        return False

def is_full():
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
print("Circular Queue:", Circular_queue)

