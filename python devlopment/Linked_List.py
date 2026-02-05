class Node:
    """A single node of the linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly Linked List implementation"""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Insert at the end"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Insert at the beginning"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """Delete a node by value"""
        current = self.head

        # If head node itself holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:  # key not found
            return

        prev.next = current.next
        current = None

    def display(self):
        """Print the linked list"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def __iter__(self):
        """Make the linked list iterable"""
        current = self.head
        while current:
            yield current.data
            current = current.next


# --------------------------
# Example usage
# --------------------------
if __name__ == "__main__":
    ll = LinkedList()

    ll.append(10)
    ll.append(20)
    ll.append(30)

    ll.prepend(5)

    ll.display()   # Output: 5 -> 10 -> 20 -> 30 -> None

    ll.delete(20)
    ll.display()   # Output: 5 -> 10 -> 30 -> None

    # Iterating using for loop
    for value in ll:
        print("Iterated:", value)