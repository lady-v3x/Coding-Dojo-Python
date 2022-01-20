class User:
    bankName = "First National Dojo"
    
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.accountBalance = 0
        
    def makeDeposit(self, amount):
        self.accountBalance = self.accountBalance + amount
        
    def makeWithdrawal(self, amount):
        self.accountBalance = self.accountBalance - amount
        
    def displayAccBal(self):
        print(f"{self.name}, Your Account Balance is {self.accountBalance}")
        
    def transferMoney(self, amount, user):
        self.accountBalance -= amount
        user.accountBalance += amount
        self.displayAccBal()
        user.displayAccBal()
    
acc1 = User("Tom R.", "Tomsthebest@everything.com")
acc2 = User("Guido van Rossum", "guido@python.com")
acc3 = User("Monty Python", "monty@python.com")
acc1.makeDeposit(10622)
acc1.makeDeposit(31)
acc1.makeDeposit(2015)
acc1.makeWithdrawal(349)
acc1.displayAccBal()
acc2.makeDeposit(500)
acc2.makeDeposit(275.50)
acc2.makeWithdrawal(30)
acc2.makeWithdrawal(20.10)
acc2.displayAccBal()
acc3.makeDeposit(730.60)
acc3.makeWithdrawal(5.05)
acc3.makeWithdrawal(10.12)
acc3.makeWithdrawal(9.10)
acc3.displayAccBal()

acc1.transferMoney(319,acc3)