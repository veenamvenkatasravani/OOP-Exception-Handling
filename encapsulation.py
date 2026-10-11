#Encapsulation means grouping data and methods together in a class and controlling how data is accessed or modified.

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def show_balance(self):
        print("Balance:", self._balance)

account = BankAccount(5000)
account.deposit(1000)
account.show_balance()

#The __balance variable is name-mangled, so accessing account.__balance directly normally raises AttributeError. Name mangling is not strict security, but it helps avoid accidental access.