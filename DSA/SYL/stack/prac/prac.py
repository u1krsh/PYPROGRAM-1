class Stack:
    def __init__(self):
        self.arr = list()
        self.length = 5
        self.top = 0
    def push(self,data):
        if self.top >= self.length:
            print("Stack is full")
        else:
            self.arr.append(data)
            self.top += 1
            print(f"Element {data} inserted")

    def pop(self):
        if self.top == 0:
            print("Stack is empty")
        else:
            self.arr.pop()
            self.top -= 1
            print("Top element popped")
    def peek(self):
        if self.top == 0:
            print("Stack is empty")
        else:
            print(self.arr[self.top-1])
    def size(self):
        if self.top == 0:
            print("Stack is empty")
        else:
            print(self.top)

arr = Stack()

arr.push(0)
arr.push(1)
arr.push(2)
arr.push(3)
arr.push(4)
arr.pop()
arr.peek()
arr.size()
arr.push(5)
arr.push(6)