#factorial custom iterator
class fact:
    def __iter__(self):
        self.num = 0
    def __next__(self):
        self.num += 1
        return self.num
f = fact()  
f_iter = iter(f)
print(next(f_iter))
