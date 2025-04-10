class Iter:
    def __init__(self,max_val):
        self.max_val = max_val

    def __iter__(self):
        return self

    def __next__(self):
        if self.max_val == 0:
            raise StopIteration
        x = self.max_val
        self.max_val -= 1
        return x

x = Iter(10)
for i in x:
    print(i,end=" ")
