#super() allows a child class to access methods from its parent class, commonly to reuse the parent's initializer.

class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def display(self):

         super().display()
         print("Marks:", self.marks)

s=Student("Sravani", 90)
s.display()