class Employee:
    company = "TechDotBit"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = Employee("Sravani")

print(Employee.company)

Employee.change_company("OpenAI")

print(Employee.company)
print(e1.company)