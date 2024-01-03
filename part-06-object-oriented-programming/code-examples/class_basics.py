# class_basics.py

class Dog:
    # Class Attribute
    species = "Canis familiaris"

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Create instances of the Dog class
dog1 = Dog("Buddy", 4)
dog2 = Dog("Lucy", 7)

# Accessing attributes
print(f"{dog1.name} is a {dog1.species}.")
print(f"{dog2.name} is a {dog2.species}.")

# Calling methods
print(dog1.description())
print(dog2.description())
print(dog1.speak("Woof Woof"))
print(dog2.speak("Bark Bark"))

# Output:
# Buddy is a Canis familiaris.
# Lucy is a Canis familiaris.
# Buddy is 4 years old
# Lucy is 7 years old
# Buddy says Woof Woof
# Lucy says Bark Bark
