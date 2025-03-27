class Stack:
    def __init__(self):
        self.data = []  

    def is_empty(self):
        return len(self.data) == 0

    def push(self, val):
        self.data.append(val)

    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        else:
            return self.data.pop()

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            for i in reversed(self.data):
                print(i, end=" ")
            print()

    def ins_at_bot(self, val):
        if self.is_empty():
            self.push(val)
        else:
            popp = self.pop()
            self.ins_at_bot(val)  
            self.push(popp)

    def rev_sta(self):
        if not self.is_empty():
            popp = self.pop()
            self.rev_sta()  
            self.ins_at_bot(popp)  

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.display()

stack.pop()
stack.ins_at_bot(69)

stack.display()

stack.rev_sta()
stack.display()
