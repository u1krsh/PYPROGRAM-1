class TwoStack:
    def __init__(self,size):
        self.size = size
        self.data = [None] * size
        self.top1 = -1
        self.top2 = size
    def push1(self,val):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.data[self.top1] = val
        else:
            print("Stack is full")
    
    