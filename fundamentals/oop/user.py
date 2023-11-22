class User:
    def __init__(self, name, email_adresse):
        self.name= name
        self.email_address = email_adresse
        self.account_balance=0
    def withdrawl(self,amount):
        if self.account_balance < amount:
            self.account_balance-=amount
            print(f"Name: {self.name} Your account balance after this transaction: {self.account_balance}")  
    def deposit(self,amount):
        self.account_balance += amount 
        print(f"Name: {self.name} Your account balance after this transaction: {self.account_balance}")
    def display_user_balance(self):
        print(f"Name: {self.name} Your account balance is: {self.account_balance}")    
    def  transfer_money(self, other_user, amount):
        if self.account_balance > amount:
            self.account_balance -= amount
            other_user.account_balance +=amount
            print("Transfert done !")
        else:
            print("The required amount is not available")


firstUser=User("Jose","jose@gmail.com")
secondUser=User("Marta","marta@yahoo.fr")
thirdUser=User("Manissa","manissa@outlook.com")

print(f"User name: {firstUser.name} Email: {firstUser.email_address} ")
print(f"User name: {secondUser.name} Email: {secondUser.email_address} ")
print(f"User name: {thirdUser.name} Email: {thirdUser.email_address} ")

firstUser.deposit(200)
firstUser.deposit(100)
firstUser.deposit(80)
secondUser.deposit(50)
secondUser.deposit(150)
secondUser.deposit(500)
thirdUser.deposit(300)
thirdUser.deposit(1000)
firstUser.withdrawl(50)
firstUser.withdrawl(90)
secondUser.withdrawl(50)
secondUser.withdrawl(100)
thirdUser.withdrawl(120)
thirdUser.withdrawl(60)
firstUser.transfer_money(secondUser,1000)
firstUser.transfer_money(secondUser,130)
secondUser.transfer_money(thirdUser,123)
secondUser.transfer_money(thirdUser,15000)