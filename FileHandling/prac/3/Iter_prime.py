def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

class Iter:
    def __init__(self, max_value):
        self.current = 1
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        while self.current <= self.max_value:
            if is_prime(self.current):
                return self.current
            self.current += 1
        raise StopIteration

# Use the iterator
for i in Iter(100):
    print(i, end=" ")
