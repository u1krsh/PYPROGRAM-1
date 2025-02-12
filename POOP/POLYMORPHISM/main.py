from abc import *

class Shape:
    @abstractmethod
    def area(self):
        pass
    

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius**2


class Square(Shape):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height
    
class Pizza(Circle):
    def __init__(self, radius, topping):
        self.topping = topping
        super().__init__(radius)
shapes = [Circle(4),Square(5),Triangle(6,7),Pizza(15,"Pepperoni")]

for i in shapes:
    print(i.area())