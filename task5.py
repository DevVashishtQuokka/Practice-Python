class BankAccount:
    account_count = 0  
 
    def __init__(self, name,balance, type):
        self.name = name
        self.balance = balance
        self.type = type
        BankAccount.account_count += 1
    def details(self):
        return {
            "Account Holder Name": self.name,
            "Balance": self.balance,
            "Account Type": self.type
        }
    def credit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} credit successfully.")
        else:
            print("Invalid amount.")
    def debit(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} debit successfully.")
        else:
            print("insufficient balance.")
    def get_balance(self):
        return self.balance
    @classmethod
    def accounts(cls):
        return cls.account_count
