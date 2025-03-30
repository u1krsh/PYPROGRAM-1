class Iterator:
    def __init__(self,start,end,step=1):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        val = self.current 
        self.current = self.current+self.step
        return val
    
f = Iterator(2,10,2)
for i in f:
    print(i,end=" ")
