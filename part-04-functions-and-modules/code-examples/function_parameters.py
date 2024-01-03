# function_parameters.py

# Function with positional parameters
def print_info(name, age):
    print(f"Name: {name}, Age: {age}")

# Calling function with positional arguments
print_info("Alice", 30)

# Function with keyword parameters
def calculate_area(length, width):
    return length * width

# Calling function with keyword arguments
area = calculate_area(length=5, width=3)
print("Area:", area)

# Function with default parameters
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Calling function with and without the default parameter
greet("Bob")
greet("Bob", greeting="Hi")

# Function with variable-length arguments (*args)
def sum_numbers(*numbers):
    return sum(numbers)

# Calling function with variable number of arguments
total = sum_numbers(1, 2, 3, 4)
print("Total Sum:", total)

# Function with variable-length keyword arguments (**kwargs)
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

# Calling function with keyword arguments
display_info(name="Alice", age=30, city="New York")

# Function with keyword-only arguments
def connect(*, host, port):
    print(f"Connecting to {host} on port {port}")

# Calling function with keyword-only arguments
connect(host="localhost", port=8080)

# End of function_parameters.py
