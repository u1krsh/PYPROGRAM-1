class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        current = self.head
        while current.next:
            current = current.next
        current.next = self.head
    def insert_at_begin(self,data):
        new_node = Node(self.head)
        new_node.next = self.head
        self.head = new_node
