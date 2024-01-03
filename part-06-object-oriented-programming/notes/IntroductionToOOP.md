# InheritanceAndPolymorphism.md

## Inheritance and Polymorphism in Python

**1. Inheritance:**

- Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).
- It provides code reusability, makes the code organized, and provides a real-world relationship between parent and child classes.
- Example:

     ```python
     class Animal:
         def __init__(self, name):
             self.name = name

         def speak(self):
             pass

     class Dog(Animal):
         def speak(self):
             return f"{self.name} says Woof!"
     ```

**2. Polymorphism:**

- Polymorphism allows methods to have the same name but behave differently in different contexts.
- In the above example, the `speak` method is implemented in each class uniquely, which is an example of polymorphism.

**3. Types of Inheritance:**

- **Single Inheritance**: When a child class inherits from only one parent class.
- **Multiple Inheritance**: When a child class inherits from multiple parent classes.
- **Multilevel Inheritance**: A form of inheritance where a class is derived from a class which is also derived from another class.

**4. Method Overriding:**

- Method overriding occurs when a method in a child class has the same name and type signature as a method in the parent class.

---

These notes provide a foundational understanding of OOP concepts in Python, essential for developing structured and scalable applications. By leveraging classes and objects, inheritance, and polymorphism, developers can write cleaner, more modular, and more maintainable Python code.
