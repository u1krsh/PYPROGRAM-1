class Car:
    
    wheels = 4
    car_number = 0
    def __init__(self,model, year, color,for_sale):
         self.model = model
         self.year = year
         self.color = color
         self.for_sale = for_sale
         Car.car_number +=1
    
    def drive(self):
        print(f"{self.model} is moving")
        
    def stop(self):
        print(f"{self.model} is stopped")
    
    def describe(self):
        print(f"Model: {self.model}, Year: {self.year}, Color: {self.color}, For Sale: {self.for_sale}")