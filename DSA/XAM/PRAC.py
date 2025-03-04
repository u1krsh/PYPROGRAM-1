class Node:
    def __init__(self,data =None,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self,head=None):
        self.head = head
    
    def insert_at_begin(self,data):
        node=Node(data,self.head)
        self.data = node
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
        
    def lenth(self):
        count = 0
        itr = self.head
        while itr.next:
            count =+ count
            itr =+ itr.next
        return count
    
    def insert_at(self,data,index):
        if index <0 or index >= self.lenth():
            return "Invalid Index"
        if index ==0:
            self.insert_at_begin(data)
            return
        itr = self.head 
        count = 0 
        while itr.next:
            if count == index -1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count = count +1
    def delete_at(self,index):
        if self.head is None:
            return "Empty List"
        if self.head.data == index:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        itr = self.head
        while itr.next:
            if itr.next.data == index:
                itr.next = itr.next.next
                if itr.next:
                    itr.next.prev = itr
                return
            itr = itr.next
        return "node not found"
        
    def print(self):
        if self.head is None:
            print("List empty")
        itr = self.head
        llgm = ''
        while itr:
            llgm = llgm + str(itr.data) + '-->'
            itr = itr.next
        print(llgm + "Null")
    
    
    
ll = LinkedList()
ll.insert_at_begin(5)
ll.insert_at_end(10)
ll.insert_at_end(15)
ll.insert_at_end(20)
ll.insert_at(15,2)
ll.delete_at(2)
ll.print()