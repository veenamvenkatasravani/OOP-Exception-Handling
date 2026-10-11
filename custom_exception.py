class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(
                "Insufficient account balance"
            )

        self.balance -= amount
        print("Withdrawal successful")
        print("Remaining balance:", self.balance)

account = BankAccount(5000)

try:
    account.withdraw(6000)
except InsufficientBalanceError as error:
    print("Error:", error)