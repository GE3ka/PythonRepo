class User:
    def __init__(self, name, email_adresse):
        self.name= name
        self.email_address = email_adresse
        self.account_balance=0
    def withdrawl(self,amount):
        if self.account_balance < amount:
            self.account_balance-=amount
            print(f"Name: {self.name} Your account balance after this transaction: {self.account_balance}")  
        return self
    def deposit(self,amount):
        self.account_balance += amount         
        print(f"Name: {self.name} Your account balance after this transaction: {self.account_balance}")
        return self
    def display_user_balance(self):
        print(f"Name: {self.name} Your account balance is: {self.account_balance}")    
    def  transfer_money(self, other_user, amount):
        if self.account_balance > amount:
            self.account_balance -= amount
            other_user.account_balance +=amount
            print("Transfert done !")
        else:
            print("The required amount is not available")
        return self    


firstUser=User("Jose","jose@gmail.com")
secondUser=User("Marta","marta@yahoo.fr")
thirdUser=User("Manissa","manissa@outlook.com")

print(f"User name: {firstUser.name} Email: {firstUser.email_address} ")
print(f"User name: {secondUser.name} Email: {secondUser.email_address} ")
print(f"User name: {thirdUser.name} Email: {thirdUser.email_address} ")

firstUser.deposit(200).deposit(100).deposit(80).withdrawl(50).withdrawl(90)
secondUser.deposit(50).deposit(150).deposit(500).withdrawl(50).withdrawl(100)
thirdUser.deposit(300).deposit(1000).withdrawl(120).withdrawl(60)
firstUser.transfer_money(secondUser,1000)
firstUser.transfer_money(secondUser,130)
secondUser.transfer_money(thirdUser,123)
secondUser.transfer_money(thirdUser,15000)
thirdUser.transfer_money(firstUser,100)
thirdUser.transfer_money(secondUser,30)