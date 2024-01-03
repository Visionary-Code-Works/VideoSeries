# inheritance_example.py

# Parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f"This animal says {sound}")

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def fetch(self, item):
        return f"{self.name} fetches the {item}"

# Creating an instance of Dog
dog = Dog("Buddy", "Canis Familiaris", "Golden Retriever")

# Accessing inherited properties and methods
print(f"{dog.name} is a {dog.species} of the breed {dog.breed}.")
dog.make_sound("Woof Woof")

# Using the child class's method
print(dog.fetch("ball"))

# Output:
# Buddy is a Canis Familiaris of the breed Golden Retriever.
# This animal says Woof Woof
# Buddy fetches the ball
