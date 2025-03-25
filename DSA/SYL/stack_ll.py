class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
    def push(self,data):
        if self.is_empty():
            self.head = Node(data)    
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
    
    def pop(self):
        if self.is_empty():
            print("Stack is emty")
        else:
            temp = self.head
            self.head = self.head.next
            print(temp.data)
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print(self.head.data)
    def display(self):
        count = self.head
        if self.is_empty():
            print("Stack is empty")
        else:
            while(count != None):
                print(count.data,"->",end="")
                count = count.next
            print("NULL")
            return
        
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.display()
stack.pop()
stack.peek()
stack.display()