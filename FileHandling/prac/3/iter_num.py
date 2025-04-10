class Iter:
    def __init__(self,max_num):
        self.max_num = max_num
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num> self.max_num:
            raise StopIteration
        even = self.num
        self.num += 2
        return even

itr = Iter(10)
for i in itr:
    print(i,end="->")

