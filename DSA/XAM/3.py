class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = self.head  # Circular link
            return
        itr = self.head
        while itr.next != self.head:  # Stop at last node
            itr = itr.next
        itr.next = node
        node.next = self.head  # Maintain circular link

    # Print the circular linked list
    def print(self):
        if self.head is None:
            print("Empty List")
            return
        itr = self.head
        llg = ''
        while True:
            llg += str(itr.data) + ' <--> '
            itr = itr.next
            if itr == self.head:  # Stop when we complete a full cycle
                break
        print(llg + '(Back to Head)')

-# Example Usage
cll = CircularLinkedList()
cll.insert(5)
cll.insert(10)
cll.insert(15)
cll.print()
