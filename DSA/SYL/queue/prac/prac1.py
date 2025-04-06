class Queue:
    def __init__(self):
        self.queue = []
    def is_empty(self):
        return len(self.queue) == 0
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        self.queue.pop(0)
    def peek(self):
        print(self.queue[0])
    def size(self):
        print(len(self.queue))
    def display(self):
        for i in self.queue:
            print(i,"|",end="")
