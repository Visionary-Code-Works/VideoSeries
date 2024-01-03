# ExceptionHandlingExercises.py

# Exercise 1: Basic Try-Except
# Write a try-except block to handle a potential "ZeroDivisionError" when dividing two numbers.
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Exercise 2: Multiple Except Blocks
# Handle different exceptions separately: "ZeroDivisionError" and "TypeError".
try:
    a = "10"
    b = 0
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero.")
except TypeError:
    print("Type error occurred.")

# Exercise 3: Try-Except-Else
# Use else block to print the result if no exceptions are raised.
try:
    x = 5
    y = 2
    result = x / y
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result: {result}")

# Exercise 4: Finally Block
# Use a finally block to print a message regardless of whether an exception occurs.
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a number.")
finally:
    print("This message is displayed no matter what.")

# Exercise 5: Raising Exceptions
# Raise a ValueError if an input is less than 0.
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
except ValueError as e:
    print(f"Error: {e}")

# Exercise 6: Custom Exception
# Create a custom exception class and use it in a function.
class NegativeAgeError(Exception):
    pass

def enter_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative.")
    print(f"Age: {age}")

try:
    enter_age(-5)
except NegativeAgeError as e:
    print(f"Caught an error: {e}")

# End of ExceptionHandlingExercises.py
