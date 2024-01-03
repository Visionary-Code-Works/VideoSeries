# polymorphism_example.py

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow"

# Polymorphism in function
def animal_sound(animal):
    print(animal.speak())

# Instances of Dog and Cat
dog = Dog()
cat = Cat()

# Same operation performed on different objects
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow
