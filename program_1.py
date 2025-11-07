class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Not enough funds')
        else:
            self.balance -= amount
    def getbalance(self):
        return self.balance
