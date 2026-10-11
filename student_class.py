class Dog:
    species = "Canine"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

    def get_info(self):
        return f"{self.name} is a {self.breed}."

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Luna", "German Shepherd")

print(dog1.name)
print(dog2.species)

print(dog1.bark())
print(dog2.get_info())



