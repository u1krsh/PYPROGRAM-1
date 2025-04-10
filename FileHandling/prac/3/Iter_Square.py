class Iter:
    def __init__(self,max_val):
        self.start = 1
        self.max_val = max_val
        self.count = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= self.max_val:
            raise StopIteration
        self.count += 1
        x = self.start
        self.start *= 2
        return x

y = Iter(10)

for i in y:
    print(i,end=" ")
