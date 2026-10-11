#Multiple inheritance means a child class inherits from more than one parent class.

class Father:
    def father_skill(self):
        print("Gardening")


class Mother:
    def mother_skill(self):
        print("Cooking")


class Child(Father, Mother):
    def child_skill(self):
        print("Programming")


c = Child()
c.father_skill()
c.mother_skill()
c.child_skill()

# child class can use methods from both father and mother