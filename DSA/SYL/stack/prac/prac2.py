class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self,data):
        if self.is_empty():
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            print("The Stack is empty")
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
            print(count.data,"->",end="")
            count=count.next

        print("NULL")
        return