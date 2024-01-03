# ClassesAndObjects.md

## Classes and Objects in Python

**1. Defining a Class in Python:**

- Classes are defined using the `class` keyword.
- A class can have properties (variables) and methods (functions).
- Example:

     ```python
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
     ```

**2. Creating Objects:**

- Objects are instances of a class created using the class name followed by parentheses.
- Example:

     ```python
     dog1 = Dog("Miles", 4)
     ```

**3. Accessing Properties and Methods:**

- Access properties using the object name followed by a dot and the property name.
- Call methods using the object name followed by a dot and the method name.
- Example:

     ```python
     name = dog1.name
     age = dog1.age
     description = dog1.description()
     ```
