class Iterator:
    def __init__(self,word):
        self.word = word
        self.index = len(word)
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return(self.word[self.index])

wrd = Iterator("sex")

for i in wrd:
    print(i,end="")