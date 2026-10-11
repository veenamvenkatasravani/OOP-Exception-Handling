# A Class is a blueprint or template used to create objects

#For example  a student class can defines students, name, age, marks, and student- related actions

#class = car blueprint
#object = actual car created from that blueprint

class student:
    name = "Sravani"
    age = 22

    def display(self):
        print(self.name)
        print(self.age)

s1 = student()
s1.display()

