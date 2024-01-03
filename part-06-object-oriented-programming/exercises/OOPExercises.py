# OOPExercises.py

# Exercise 1: Basic Class Definition
# Define a class named "Car" with an instance variable "brand" and a method that prints "This is a [brand] car."
class Car:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print(f"This is a {self.brand} car.")

# Creating an instance of Car and using it
my_car = Car("Toyota")
my_car.display()

# Exercise 2: Inheritance
# Define a class "ElectricCar" that inherits from "Car" and adds a new method to display battery level.
class ElectricCar(Car):
    def __init__(self, brand, battery_level):
        super().__init__(brand)
        self.battery_level = battery_level

    def display_battery(self):
        print(f"Battery level: {self.battery_level}%")

# Creating an instance of ElectricCar and using it
my_electric_car = ElectricCar("Tesla", 85)
my_electric_car.display()
my_electric_car.display_battery()

# Exercise 3: Polymorphism
# Define a method in Car called "fuel_type" and override it in ElectricCar.
class Car:
    def fuel_type(self):
        print("This car uses gasoline.")

class ElectricCar(Car):
    def fuel_type(self):
        print("This car is electric.")

# Demonstrating polymorphism
my_car = Car()
my_electric_car = ElectricCar()
my_car.fuel_type()
my_electric_car.fuel_type()

# Exercise 4: Encapsulation
# Modify the ElectricCar class to make the battery_level a private attribute with a public method for updating it.
class ElectricCar(Car):
    def __init__(self, brand, battery_level):
        super().__init__(brand)
        self.__battery_level = battery_level

    def update_battery(self, new_level):
        self.__battery_level = new_level
        print(f"Updated battery level: {self.__battery_level}%")

# Updating battery level using the public method
my_electric_car = ElectricCar("Nissan", 70)
my_electric_car.update_battery(90)

# End of OOPExercises.py
