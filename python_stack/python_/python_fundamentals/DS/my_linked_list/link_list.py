class SLNode:
    """Represents a single node in a singly linked list."""
    def __init__(self, val):
        self.value = val
        self.next = None


class SList:
    """Represents a Singly Linked List."""
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        """Adds a new node to the front of the list."""
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self  # Allows method chaining

    def add_to_back(self, val):
        """Adds a new node to the end of the list."""
        if self.head is None:
            self.add_to_front(val)
            return self
        
        new_node = SLNode(val)
        runner = self.head
        while runner.next is not None:
            runner = runner.next
        runner.next = new_node
        return self

    def print_values(self):
        """Prints all node values in the list."""
        runner = self.head
        while runner is not None:
            print(runner.value)
            runner = runner.next
        return self


# Test the code
if __name__ == "__main__":
    my_list = SList()
    my_list.add_to_front("are") \
         .add_to_front("Linked lists") \
           .add_to_back("fun!") \
           .print_values()
           
