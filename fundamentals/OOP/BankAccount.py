class BankAccount:
    allAccs = []

    def __init__(self, int_rate, balance ):
            self.int_rate = int_rate
            self.balance = balance
            BankAccount.allAccs.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds! Charging $5 fee")
            self.balance -= 5
        return self

    def displayAccInfo(self):
        print(f"Your current Balance is: ${self.balance}")
        return self

    def yieldInterest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def allAccounts(cls):
        for account in cls.allAccs:
            account.displayAccInfo()

T = BankAccount(.095,12319)
W = BankAccount(.095,10500)

T.deposit(1875.50).deposit(2100).deposit(1990.25).withdraw(1200).yieldInterest()
W.deposit(775).deposit(2021.90).withdraw(25).withdraw(50).withdraw(75).withdraw(100).yieldInterest()

BankAccount.allAccounts()