
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

class User:
    def __init__(self, name, email_adresse):
        self.name= name
        self.email_address = email_adresse
        self.account = BankAccount(int_rate=0.02, balance=0)
    def withdrawl(self,amount):
        if self.account.balance< amount:
            self.account.balance-=amount
            print(f"Name: {self.name} Your account balance after this transaction: {self.account.balance}")  
    def deposit(self,amount):

        self.account.balance += amount 
        print(f"Name: {self.name} Your account balance after this transaction: {self.account.balance}")
    def display_user_balance(self):
        print(f"Name: {self.name} Your account balance is: {self.account.balance}")    
    def  transfer_money(self, other_user, amount):
        if self.account.balance > amount:
            self.account.balance -= amount
            other_user.account.balance +=amount
            print("Transfert done !")
        else:
            print("The required amount is not available")
myBank=BankAccount(0.01,0)  
print(f"Bank Name: {myBank.bankName}")   
firstUser=User("jose","jose@gmail.com")  
firstUser.account.reference="001"
firstUser.deposit(500) 
firstUser.display_user_balance()    
myBank.display_all_accounts() 
