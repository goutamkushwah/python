Double_Queue= []
Max=10
# Enqueue Front
def Enqueue_Front(item):
    if len(Double_Queue) < Max:
        Double_Queue.insert(0, item)
        print(f"Enqueued {item} to front of double queue")
    else:
        print("Double Queue Overflow")
# Enqueue Rear
def Enqueue_Rear(item):
    if len(Double_Queue) < Max:
        Double_Queue.append(item)
        print(f"Enqueued {item} to rear of double queue")
    else:
        print("Double Queue Overflow")
# Dequeue Front
def Dequeue_Front():
    if len(Double_Queue)==0:
        print("Double Queue Underflow")
    else:
        item = Double_Queue.pop(0)
        print("Dequeued item from front:", item)
# Dequeue Rear
def Dequeue_Rear():
    if len(Double_Queue)==0:
        print("Double Queue Underflow")
    else:
        item = Double_Queue.pop()
        print("Dequeued item from rear:", item)
def size():
    return len(Double_Queue)
def front():
    if len(Double_Queue)==0:
        print("Double Queue is empty")
    else:
        return Double_Queue[0]
    
def rear():
    if len(Double_Queue)==0:
        print("Double Queue is empty")
    else:
        return Double_Queue[-1]
def is_empty():
    if len(Double_Queue)==0:
        return True
    else:
        return False
def is_full():
    if len(Double_Queue)==Max:
        return True
    else:
        return False
    
Enqueue_Front(10)
Enqueue_Rear(20)    
Enqueue_Front(30)
print("Front element:", front())
print("Rear element:", rear())
print("Size:", size())
Dequeue_Front()
Dequeue_Rear()
print("Is empty?", is_empty())
print("Is full?", is_full())
print("Double Queue:", Double_Queue)
