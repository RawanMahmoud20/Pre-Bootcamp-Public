class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        
        return f"${self.balance}"

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
      
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
        
    def display_user_balance(self):
        balance = self.account.display_account_info()
        print(f"The User Is: {self.name} | Balance: {balance}")
        return self

    def transfer_money(self, other_user, amount):
        if self.account.balance >= amount:
            self.account.withdraw(amount)
            other_user.account.deposit(amount)
            print(f"Transferring ${amount} from {self.name} to {other_user.name}")
        else:
            print(f"Not enough balance for {self.name}")
        return self


rawan = User("Rawan", "Rawan@gmail.com")    
shath = User("shath", "shath@gmail.com")    
manar = User("manar", "manar@gmail.com")

rawan.make_deposit(100).make_withdrawal(200).display_user_balance()
shath.make_deposit(2000).make_withdrawal(500).display_user_balance()

shath.transfer_money(rawan, 200)

rawan.display_user_balance()
shath.display_user_balance()
class UserWithMultipleAccounts:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {
            "savings": BankAccount(int_rate=0.05, balance=0),
            "checking": BankAccount(int_rate=0.01, balance=0)
        }

    def make_deposit(self, amount, account_type="checking"):
        self.accounts[account_type].deposit(amount)
        return self

    def display_user_balance(self):
        print(f"Accounts for {self.name}")
        for type, acc in self.accounts.items():
            print(f"{type}: ${acc.balance}")
            acc.display_account_info()
        return self


ali = UserWithMultipleAccounts("Ali", "ali@gmail.com")
ali.make_deposit(100, "savings").make_deposit(50, "checking").display_user_balance()