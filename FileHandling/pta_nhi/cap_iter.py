class Iterator:
    def __init__(self,word):
        self.word = word
        self.index = 0
        
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.word):
            raise StopIteration
        word = self.word[self.index]
        if self.index % 2 == 0:
            result = word.upper()
        else:
            result = word.lower()
        self.index +=1
        return result

word = ["hello", "world", "python", "iterators", "example"]
for i in Iterator(word):
    print(i,end=" ")