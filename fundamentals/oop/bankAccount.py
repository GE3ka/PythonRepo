class BankAccount:
    bankName="Dojo National Bank"
    all_bank_accounts=[]
    def __init__(self, int_rate, balance): 
        self.int_rate= int_rate
        self.balance=balance
        self.reference="000"
        BankAccount.all_bank_accounts.append(self)
    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if self.balance<amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance-=amount
        return self        
    def display_account_info(self):
        print(f"Balance ${self.balance}")
    def yield_interest(self):
        if self.balance>0:
            self.balance+= self.balance * self.int_rate
        return self
    @classmethod
    def display_all_accounts(cls):
        print(f"******{BankAccount.bankName}********")
        for account in cls.all_bank_accounts:
            print (f"Reference: {account.reference} Balance: {account.balance}")

first_account=BankAccount(0.01,0)
first_account.reference="001"
second_account=BankAccount(0.02,30)
second_account.reference="002"
first_account.deposit(300).deposit(120).deposit(190).withdraw(350).yield_interest().display_account_info()
second_account.deposit(500).deposit(170).withdraw(20).withdraw(50).withdraw(150).withdraw(35).yield_interest().display_account_info()

BankAccount.display_all_accounts()