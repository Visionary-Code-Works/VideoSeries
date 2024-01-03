# FunctionsExercises.py

# Exercise 1: Basic Function
# Define a function named greet that prints "Hello, World!"
def greet():
    print("Hello, World!")

greet()  # Calling the function

# Exercise 2: Function with Arguments
# Define a function that takes a name as an argument and prints "Hello" followed by the name.
def greet_name(name):
    print(f"Hello, {name}")

greet_name("Alice")  # Example usage

# Exercise 3: Function with Return Value
# Define a function that takes two numbers as arguments and returns their sum.
def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(5, 3)
print("Sum:", result)  # Should print the sum of the numbers

# Exercise 4: Function with Multiple Return Values
# Define a function that takes a list and returns both its maximum and minimum values.
def find_max_min(lst):
    return max(lst), min(lst)

max_val, min_val = find_max_min([1, 2, 3, 4, 5])
print("Max:", max_val, "Min:", min_val)

# Exercise 5: Recursive Function
# Write a recursive function to calculate the factorial of a number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# Exercise 6: Function with Default Arguments
# Define a function that prints a greeting message. It should have a default name to greet if no name is provided.
def greet_default(name="World"):
    print(f"Hello, {name}!")

greet_default()       # Should print "Hello, World!"
greet_default("Bob")  # Should print "Hello, Bob!"

# Exercise 7: Lambda Function
# Create a lambda function that takes one argument (x) and returns its square.
square = lambda x: x * x
print("Square of 4:", square(4))

# End of FunctionsExercises.py
