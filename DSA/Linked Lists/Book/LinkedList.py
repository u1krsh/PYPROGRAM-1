#pg 390

from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    def insertBegin(self, value):
        if self.head is not None:
            self.head=Node(value)
        else:
            temp = Node(value)
            temp.next = self.head
            self.head = temp
        print("Value Inserted")
        