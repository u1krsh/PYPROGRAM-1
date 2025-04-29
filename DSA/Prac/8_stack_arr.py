class Stack:
    def __init__(self):
        self.stack  = []
    def is_empty(self):
        return  len(self.stack) == 0

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()
    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

