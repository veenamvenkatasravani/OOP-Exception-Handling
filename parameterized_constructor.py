class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary =salary

    def display(self):
        print("Name:", self.name)
        print("Salalry:", self.salary)

e1 = Employee("Sravani", 25000)
e2 = Employee("Ravi", 30000)

e1.display()
e2.display()