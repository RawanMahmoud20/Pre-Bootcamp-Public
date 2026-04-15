class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"The User Is: {self.name} Have a balance: {self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"--- Transferring ${amount} from {self.name} to {other_user.name} ---")


# Users
Rawan = User("Rawan", "Rawan@gmail.com")
shath = User("shath", "shath@gmail.com")
manar = User("manar", "manar@gmail.com")

# Rawan operations
Rawan.make_deposit(100)
Rawan.make_withdrawal(200)
Rawan.make_deposit(50)
Rawan.make_withdrawal(45)
Rawan.display_user_balance()

# Shath operations
shath.make_deposit(1000)
shath.make_deposit(1000)
shath.make_withdrawal(500)
shath.make_withdrawal(300)
shath.display_user_balance()

# Manar operations
manar.make_deposit(500)
manar.make_withdrawal(100)
manar.make_withdrawal(100)
manar.make_withdrawal(50)
manar.display_user_balance()

# Transfer money
shath.transfer_money(Rawan, 200)

# Final balance
Rawan.display_user_balance()