# basic_functions.py

# Function with no parameters
def greet():
    print("Hello, welcome to Python!")

# Calling the function
greet()

# Function with one parameter
def greet_name(name):
    print(f"Hello, {name}! Welcome to Python!")

# Calling the function with a parameter
greet_name("Alice")

# Function with two parameters
def add_numbers(num1, num2):
    return num1 + num2

# Calling the function and printing the result
result = add_numbers(5, 3)
print(f"The sum of 5 and 3 is {result}")

# Function with a default parameter value
def greet_with_default(name="there"):
    print(f"Hello, {name}!")

# Calling the function with and without a parameter
greet_with_default("Bob")
greet_with_default()

# Function that returns a formatted string
def create_greeting(name):
    return f"Hello, {name}! Have a great day!"

# Using the returned value from the function
greeting = create_greeting("Alice")
print(greeting)

# End of basic_functions.py
