class Queue:
    def __init__(self):
        self.elems = []

    # adds element to the back
    def enqueue(self, val):
        self.elems.append(val)

    # removes element from the front
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.elems.pop(0)

    # view the front element
    def peek(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.elems[0]

    # get size
    def size(self):
        return len(self.elems)

    # check if empty
    def is_empty(self):
        return len(self.elems) == 0


# تجربة
my_queue = Queue()
my_queue.enqueue("Ali")
my_queue.enqueue("Sara")
my_queue.enqueue("Rawan")

print(my_queue.peek())    # Ali
print(my_queue.size())    # 3
print(my_queue.dequeue()) # Ali
print(my_queue.peek())    # Sara
print(my_queue.size())    # 2