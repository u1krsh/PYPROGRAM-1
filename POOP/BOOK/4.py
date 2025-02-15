class Bank:
    def __init__(self,name,account_number,type,amount=0):
        self.name = name
        self.account_number = account_number
        self.type = type
        self.amount = amount
        
    def deposit(self,amount):
        self.amount = amount
        
    def withdraw(self,amount):
        self.amount = self.amount - amount
        
    def interest(self):
        if self.amount >= 500000:
            self.interest = 8.0
        elif self.amount >= 300000:
            self.interest = 7.0
        elif self.amount >=100000:
            self.interest = 5.0
        else:
            self.interest = 3.0
    def __str__(self):
        return f"Name: {self.name} Acc no.{self.account_number} Acc Type: {self.type} Amount: {self.amount} Interest: {self.interest}"
    

per1 = Bank("Shaun", 69420, "Saving Account")
per1.deposit(1000000)
per1.withdraw(1000)
per1.interest()

print(per1)
    