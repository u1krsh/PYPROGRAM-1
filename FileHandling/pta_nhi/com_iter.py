class Iterator:
    def __init__(self,max_val):
        self.max_val = max_val
        self.num = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.num > self.max_val:
            raise StopIteration
        even = self.num
        self.num = self.num + 2
        return even

evens = Iterator(20)
for i in evens:
    print(i,end=" ")
