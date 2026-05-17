class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initializes the object with the size of the queue to be k.
        """
        self.queue = [None] * k
        self.capacity = k
        self.head = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        """
        Inserts an element into the circular queue. Return true if successful.
        """
        if self.isFull():
            return False
        
        # Calculate the next insertion index (tail) using modulo
        tail_idx = (self.head + self.size) % self.capacity
        self.queue[tail_idx] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        """
        Deletes an element from the circular queue. Return true if successful.
        """
        if self.isEmpty():
            return False
        
        # Move head to the next position using modulo
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        """
        Gets the front item from the queue. If empty, return -1.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """
        Gets the last item from the queue. If empty, return -1.
        """
        if self.isEmpty():
            return -1
        # Calculate the exact current tail index
        tail_idx = (self.head + self.size - 1) % self.capacity
        return self.queue[tail_idx]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.capacity