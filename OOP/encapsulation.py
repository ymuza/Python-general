"""
encapsulation is the building of data, along with the methods that operate that data
into a single unit (generally a class). No one can access the data inside the class, from
the outside of the class, so we can restrict the access. This prevents data inside
the class from being modified.
"""

class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # "protected" attribute (convention)

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

# Usage
account = BankAccount(100)
account.deposit(50)
print(account.get_balance())  # 150

# Direct access is discouraged but possible
print(account._balance)  # 150 (works but not recommended)

