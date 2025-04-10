class Iter:
    def __init__(self,max_val):
        self.max_val = max_val
        self.a,self.b = 0,1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_val:
            raise StopIteration
        self.count += 1
        fib = self.a
        self.a,self.b = self.b, self.a+self.b
        return fib

x = Iter(1000)
for i in x:
    print(i,end=" ")