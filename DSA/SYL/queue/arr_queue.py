class Queue:
    
    def __init__(self):
        self.item = []
        
    def is_empty(self): 
        return len(self.item) == 0
    
    def enqueue(self,data):
        self.item.append(data)
    
    def dequeue(self):
        self.item.pop(0)
    
    def peek(self):
        return self.item[0]
    
    def size(self):
        return len(self.item)
    
    def display(self):
        for i in self.item:
            print(i,'|',end="")
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.dequeue()
print(queue.peek())
print(queue.size())
queue.display()