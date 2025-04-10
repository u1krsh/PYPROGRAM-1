class Iter:
    def __init__(self,str):
        self.str =str
        self.index = len(str)
    def __iter__(self):
        return  self

    def __next__(self):
        if self.index ==0:
            raise StopIteration
        self.index -= 1
        return self.str[self.index]

s = Iter("Hello")
for i in s:
    print(i,end="")
