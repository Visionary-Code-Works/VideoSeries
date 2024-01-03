# To use this file:

# 1. Save the above code in a file named BasicExercises.py.
# 2. Run the script using a Python interpreter. The script will execute each exercise in sequence, demonstrating basic Python functionalities.
# 3. You can comment out or modify sections to experiment with the code.

# BasicExercises.py

# Exercise 1: Hello World
# Print "Hello, World!" to the console
print("Hello, World!")

# Exercise 2: Variables and Input
# Ask the user for their name and then greet them with their name.
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Exercise 3: Simple Arithmetic
# Ask the user for two numbers, then print the sum of those numbers.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}")

# Exercise 4: List Operations
# Create a list of 3 elements, then add a fourth element, and print the list.
my_list = [1, 2, 3]
my_list.append(4)
print(f"Updated list: {my_list}")

# Exercise 5: Conditional Logic
# Check if a number is positive, negative, or zero.
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Exercise 6: Looping Through a Range
# Print numbers from 1 to 5 using a for loop.
for i in range(1, 6):
    print(i)

# Exercise 7: Functions
# Define a function that takes two numbers as arguments and returns their product.
def multiply(x, y):
    return x * y

product = multiply(4, 5)
print(f"The product of 4 and 5 is {product}")

# End of BasicExercises.py
