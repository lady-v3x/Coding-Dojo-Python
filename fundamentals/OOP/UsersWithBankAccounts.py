class BankAccount:
    allAccs = []

    def __init__(self, int_rate, balance):
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
        
    def yieldInterest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def allAccounts(cls):
        for account in cls.allAccs:
            account.displayAccInfo()

class User:

    def __init__(self, name):
        self.name = name
        self.account = {
            "checking" : BankAccount(.05,1500),
            "savings" : BankAccount(.07,10000)
        }
        
    def displayUserBalance(self):
        print(f"{self.name}, Your Current Checking Balance is: ${self.account['checking'].balance}")
        print(f"{self.name}, Your Current Savings Balance is: ${self.account['savings'].balance}")
        return self

    def transferMoney(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.displayUserBalance()
        user.displayUserBalance()
        return self

T = User("Tom")
W = User("Watkins")

T.account['checking'].deposit(18707).withdraw(7).yieldInterest()
T.account['savings'].deposit(450).yieldInterest()
W.account['checking'].deposit(13894).withdraw(94).yieldInterest()
W.account['savings'].deposit(475).yieldInterest()
T.displayUserBalance()
W.displayUserBalance()