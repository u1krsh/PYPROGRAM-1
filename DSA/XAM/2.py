class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_begin(self, data):
        node = Node(data)
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node

    # Insert at the end
    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node  # Fix: Initialize the head if list is empty
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node
        node.prev = itr  

    # Delete node by value
    def delete_by_value(self, value):
        if self.head is None:
            print("Empty List")
            return
        if self.head.data == value:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        itr = self.head
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                if itr.next:
                    itr.next.prev = itr
                return
            itr = itr.next
        print("Node not found")

    # Print Linked List
    def print(self):
        if self.head is None:
            print("List is Empty")
            return
        itr = self.head
        llg = ''
        while itr:
            llg += str(itr.data) + ' <--> '
            itr = itr.next
        print(llg + 'Null')

# Example Usage
dll = LinkedList()
dll.insert_at_begin(5)
dll.insert_at_begin(7)
dll.insert_at_end(8)
dll.delete_by_value(8)  # Fix: Renamed function
dll.print()
