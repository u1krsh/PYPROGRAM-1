class Bank:
    def __init__(self,acc_num,balance = 0):
        self.acc_num = acc_num
        self.balance = balance

    def deposit(self,amt):
        self.balance += amt
        print(f"{amt} rupees deposited in account: {self.acc_num} total balance: {self.balance}")

    def withdraw(self,amt):
        self.balance -= amt
        print(f"{amt} rupees withdrawn from account: {self.acc_num} total balance: {self.balance}")

    def ckc_bal(self):
        print(f"Your current balance is {self.balance} rupees ")

acc1 = Bank(1234,2000)
acc1.deposit(2000)
acc1.withdraw(500)
acc1.ckc_bal()
