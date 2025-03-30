class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear - 1
        self.size = 0
    def is_empty(self):
        return self.size == 0
    def is_full(self):
        return self.size == self.capacity
    
    def enqueue(self,data):
        if self.is_full():
            print("Queue is full")
            return
        if(self.is_empty()):
            self.rear = self.front = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear]
        self.size += 1
        
    def dequeue(self):
        