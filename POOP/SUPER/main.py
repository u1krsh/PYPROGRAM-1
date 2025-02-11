class Shape:
    def __init__(self,color,filled):
        self.color = color
        self.filled = filled


class Circle(Shape):
    def __init__(self,color,filled,radius):
        super().__init__(color, filled)
        self.radius = radius
        

class Square(Shape):
    def __init__(self,color,filled,width):
        super().__init__(color, filled)
        self.widht = width

class Triangle(Shape):
    def __init__(self,color,filled,widht,height):
        super().__init__(color, filled)
        self.width = widht
        self.height = height
    
circle = Circle("red",True,5)

print(circle.color)