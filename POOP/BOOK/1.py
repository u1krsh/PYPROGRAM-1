class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def setLenth(self,length):
        self.length = length
    
    def setBreadth(self,breadth):
        self.breadth = breadth
    
    def area(self):
        print(f"Area is {self.length*self.breadth}")
    
    def perimeter(self):
        print(f"Perimeter is {2*(self.length+self.breadth)}")
    def retValue(self):
        print(f"Length: {self.length},breadth: {self.breadth}")

rec =Rectangle(2,5)

rec.retValue()
rec.setLenth(10)
rec.retValue()
rec.setLenth(11)
rec.retValue()
rec.area()
rec.perimeter()