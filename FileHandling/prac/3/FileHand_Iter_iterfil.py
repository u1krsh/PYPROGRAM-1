class Iter:
    def __init__(self,filename):
        self.file = open("report.txt", "r")


    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        return line.strip()

