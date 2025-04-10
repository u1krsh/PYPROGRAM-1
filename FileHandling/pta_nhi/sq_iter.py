class Iterator:
    def __init__(self,num):
        self.num = num
        self.count = 0
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.count > self.num:
            raise StopIteration
        val = self.count * self.count
        self.count = self.count + 1
        return val
ff = Iterator(10)
for i in ff:
    print(i,end=" ")

