class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ₹{amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ₹{amount}")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance

    def display(self):
        print("Account Number:", self.__account_number)
        print("Account Holder:", self.__holder_name)
        print("Balance: ₹", self.__balance)

class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance, interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        print("Savings Account Deposit")
        super().deposit(amount)

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        super().deposit(interest)
        print(f"Interest added: ₹{interest:.2f}")

class CurrentAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance, overdraft_limit):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance() + self.overdraft_limit:
            if amount <= self.get_balance():
                super().withdraw(amount)
            else:
                remaining = amount - self.get_balance()
                super().withdraw(self.get_balance())
                print(f"Overdraft used: ₹{remaining}")
        else:
            print("Overdraft limit exceeded")

def show_account(account):
    account.display()
    print("Current Balance: ₹", account.get_balance())
    print("-" * 30)

# Main program
savings = SavingsAccount("101", "Komal", 10000, 5)
current = CurrentAccount("102", "Rahul", 5000, 2000)

print("=== Savings Account ===")
savings.deposit(2000)
savings.add_interest()
savings.withdraw(1000)
show_account(savings)

print("=== Current Account ===")
current.deposit(1000)
current.withdraw(7000)
show_account(current)

print("=== Polymorphism ===")
accounts = [savings, current]

for account in accounts:
    show_account(account)