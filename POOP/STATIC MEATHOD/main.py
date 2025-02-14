class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position
        
    def get_info(self):
        return f"{self.name} is a {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_postions = ["Manager","Cashier","Cook","Janitor"]
        return position in valid_postions
    
print(Employee.is_valid_position("Cook"))