class Node:
    def __init__(self,data=None,next =None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self,head=None):
        self.head = head
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
            
    def insert_list(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)
            
    def length(self):
        count = 0
        itr= self.head 
        while itr.next:
            count = count +1
            itr = itr.next
        return count
    def remove_at(self,index):
        if index <0 or index >= self.length():
            return "Invalid index"
        if index == 0:
            self. head = self.head.next
            
        count = 0
        itr = self.head
        while itr.next:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count = count +1
            
            
    def insert_at(self,index,data):
        if index < 0 or index >= self.length():
            return "Invalid index"
        if index ==0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head 
        while itr.next:
            if count == index -1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count = count +1
            

    def print(self):
        if self.head is None:
            print("List is empty")
        
        itr = self.head
        llg = ''
        while itr:
            llg = llg+ str(itr.data) + ' --> '
            itr = itr.next
        print(llg+"Null")       
    
l = LinkedList()
l.insert_at_begining(5)
l.insert_at_begining(8)
l.insert_at_end(9)
l.print()
