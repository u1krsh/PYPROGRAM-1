class pow2:
    def __init__(self,max=0):
        self.max = max
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result

a = pow2(2)
i =iter(a)
print(next(i))

