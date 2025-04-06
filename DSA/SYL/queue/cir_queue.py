class Node:
    def __init__(self, val, nxt, prev):
        self.val = val
        self.next = nxt
        self.prev = prev
class Queue:
    def __init__(self,k):
        self.space = k
        self.left = Node(0,None,None)
        self.right = Node(0,None,self.left)
        self.left.next = self.right
    def is_empty(self):
        return self.left.next == self.right
    def is_full(self):
        return self.space == 0
    def peek(self):
        if self.is_empty():
            print("queue is empty")
        else:
            return self.left.next.val
    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
        else:
            cur = Node(value,self.right,self.right.prev)
            self.right.prev.next = cur
            self.right.prev = cur
            self.space -=1
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            self.left.next = self.left.next.next
            self.left.next.prev = self.left
            self.space += 1
