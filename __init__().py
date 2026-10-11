#__init__() is an initializer method that runs automatically when a new object is created. It is commonly called the constructor in beginner-level explanations.

class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


e1 = Employee("Sravani", 25000)
e2 = Employee("Sandhya", 30000)

e1.display()
e2.display()