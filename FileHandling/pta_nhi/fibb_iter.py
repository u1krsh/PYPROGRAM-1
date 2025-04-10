class Iterator:
    def __init__(self,max):
        self.max = max
        self.a,self.b = 0,1
        self.count = 0
    def __iter__(self): 
        return self
    
    def __next__(self):
        if self.count>self.max:
            raise StopIteration
        self.count = self.count + 1
        fib = self.a
        self.a,self.b =self.b,self.a+self.b
        return fib
fibb = Iterator(15)
for i in fibb:
    print(i,end=",")
        