class Stack:
    def __init__(self):
        self.arr = list()
        self.length = 5
        self.top = 0
        
    def push(self,data):
        if self.top >= self.length:
            return("Stack is full")
        else:
            self.arr.append(data)
            self.top += 1
            return "element inserted"
    def pop(self):
        if self.top == 0:
            return("Stack is empty")
        else:
            self.arr.pop()
            self.top -= 1
            return "element popped"
    def peek(self):
        if self.top == 0:
            return("Stack is empty")
        else:
            return(self.arr[self.top-1])
            
    def size(self):
        return self.top
    
    def display(self):
        return self.arr

stack = Stack()

print(stack.push(1))
print(stack.push(2))
print(stack.push(3))
print(stack.push(4))
print(stack.push(5))
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.size())
print(stack.display())