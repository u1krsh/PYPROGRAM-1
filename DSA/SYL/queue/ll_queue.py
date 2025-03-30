class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        
    def is_empty(self):
        return self.front is None
    
    def enqueue(self,data):
        newnode = Node(data)
        if self.is_empty():
            self.front = newnode
            self.back = newnode
        else:
            self.back.next = newnode
            self.back = newnode
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            del_item = self.front
            self.front = self.front.next
            if self.front is None:
                self.back  = None
            return del_item

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.front.data
    def size(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            count = 1
            current = self.front
            while current:
                count += 1
                current = current.next
            return count
        
    def display(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            current = self.front
            while current:
                print(current.data,"|",end="")
                current = current.next
            print()

        
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.display()
print(queue.peek())
print(queue.size())
queue.dequeue()
queue.display()
print(queue.peek())
print(queue.size())