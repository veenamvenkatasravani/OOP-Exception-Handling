#Instance variables belong to individual objects. Each object can store different values.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


s1 = Student("Sravani", 90)
s2 = Student("Ravi", 80)

print(s1.name, s1.marks)
print(s2.name, s2.marks)