class User:
    def __init__(self, name , email):
        self.name = name
        self.email = email
        self.account_balance = 0
        
    
    def make_deposit(self , amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
        
    def display_user_balance(self):
        print(f"The User Is: {self.name} Hava a balance: {self.account_balance} ")
        return self
    def trasfer_money(self , other_user , amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"--- Transferring ${amount} from {self.name} to {other_user.name} ---")
        return self
        

Rawan= User("Rawan", "Rawan@gmail.com")    
shath= User("shath", "shath@gmail.com")    
manar= User("manar", "manar@gmail.com")
# Rawan operations
    
Rawan.make_deposit(100).make_withdrawal(200).make_deposit(50).make_withdrawal(45).display_user_balance()
# Shath operations

shath.make_deposit(1000).make_deposit(1000).make_withdrawal(500).make_withdrawal(300).display_user_balance()
# manar operations
manar.make_deposit(500).make_withdrawal(100).make_withdrawal(100).make_withdrawal(50).display_user_balance()

# Transfer money

shath.trasfer_money(Rawan, 200)
Rawan.display_user_balance()
shath.display_user_balance()

