class Item:
    def __init__(self,name,price,quantity):
            self.name = name
            self.price = price
            self.quantity = quantity
            
    def purchase(self,quantity):
        self.quantity = self.quantity - quantity
    
    def increaseStock(self,quantity):
        self.quantity = self.quantity + quantity
    def display(self):
        return f"Name: {self.name} Price: {self.price} Quantity: {self.quantity}"
    
    
s1 = Item("Banana",20.0,100)
s1.purchase(10)

s1.increaseStock(50)

print(s1.display())
    
    