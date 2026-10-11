class Employee:
    company = "TechDotBit"

    def __init__(self, name):
        self.name = name


e1 = Employee("Sravani")
e2 = Employee("Ravi")

print(e1.name)
print(e2.name)
print(e1.company)
print(e2.company)
print(Employee.company)