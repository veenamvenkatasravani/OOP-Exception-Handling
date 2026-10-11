class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Student:", self.name)


s1 = Student("Sravani")
s2 = Student("Ravi")

s1.show()
s2.show()