class Engine:
    def __init__(self,horsepower):
        self.horsepower = horsepower

class Wheel:
    def __init__(self, size):
        self.size = size
class Car:
    def __init__(self,make,model,horsepower,size):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)
        self.wheels = [Wheel(size) for wheel in range(4)]
     
    def display(self):
        return f"{self.make},{self.model},{self.horsepower},{self.engine}"
car = Car('Toyota','Corolla',100,15)

print(car.display())