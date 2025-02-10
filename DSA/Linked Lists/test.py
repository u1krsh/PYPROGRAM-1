class node:
    def __init__(self,data = 0):
        self.data= data #pass data point 
        self.next = None # pointer to next node
        
class linked_list:
    def __init__(self):
        self.head = node() # pointer to head node 

#append function
    def append(self,data):
        new_node = node(data) #new node
        curr = self.head #current node
        while curr.next != None: #while current node next element is not none
            curr = curr.next  #traverse node
        curr.next = new_node #add new node at the end of the list

#lenth function
    def lenth(self):
        curr  = self.head #current node
        total = 0
        while curr.next != None: #while current node next element is
            total += 1
            curr = curr.next  #traverse node
        print(total)
#display fucntion
    def display(self):
        elems = [] #list to store elements
        curr_node = self.head #current node
        while curr_node.next is not None: #while current node next element is not none
            curr_node = curr_node.next #traverse node
            elems.append(curr_node.data) #add node data to the list
        print(elems)
        
#get fucn
    def get(self, index):
        if index < 0:
            print("Index cannot be negative")
            return None  
        curr_index = 0  # Current index
        curr = self.head  # Current node
        while curr is not None:
            if curr_index == index:
                return curr.data
            curr = curr.next
            curr_index += 1
            print(curr_index) 
        print("Index out of range")
        return None
                
#delete fucn
    def delete(self, index):
        if index < 0:
            print("Index cannot be negative")
            return None
        curr_index = 0
        curr_node = self.head
        while curr_node is not None:
            last_node = curr_node # Last node is the current node
            curr_node = curr_node.next 
            if curr_index == index:
                last_node.next = curr_node.next 
                return
            else: curr_index += 1
        print("Index Out of range")
        return None       
        

   
my_list = linked_list()

my_list.append(1)
my_list.display()
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
my_list.lenth()
print("List length")
my_list.get(1)

my_list.delete(6)

my_list.display()

 