class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def add_to_back(self, value):
        """Adds a new node to the end of the list."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return self

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

        return self


    def add_to_front(self, value):
        """Adds a new node to the beginning of the list."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return self

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

        return self


    def traverse_forward(self):
        """Prints all values from head to tail."""
        current = self.head

        while current: 
            print("the value is : " , current.value)
            current = current.next

        return self


    def traverse_backward(self):
        """Prints all values from tail to head."""
        current = self.tail
        values = []

        while current:
            values.append(str(current.value))
            current = current.prev

        print("Backward: " + " <-> ".join(values))
        return self
 
 
dll = DoubleLinkedList()

dll.add_to_front(10)
dll.add_to_front(5)
dll.add_to_back(20)
dll.add_to_back(30)

dll.traverse_forward()
dll.traverse_backward() 
    