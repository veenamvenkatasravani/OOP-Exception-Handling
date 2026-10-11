#Abstraction exposes essential functionality while hiding implementation details. Python supports abstraction through the abc module.

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} using UPI")

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} using Card")

p1 = UpiPayment()
p2 = CardPayment()

p1.pay(500)
p2.pay(1000)