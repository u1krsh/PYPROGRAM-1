class Iter:
    def __init__(self,start,end,gap=1):
        self.start = start
        self.end = end
        self.gap = gap


    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration

        x = self.start
        self.start += self.gap
        return x
x =Iter(2,10,2)
for i in x:

    print(i,end=" ")


