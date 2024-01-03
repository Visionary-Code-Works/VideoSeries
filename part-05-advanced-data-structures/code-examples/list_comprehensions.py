# list_comprehensions.py

# Basic List Comprehension - Generating a list of squares
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# Conditional List Comprehension - Generating a list of even numbers
evens = [x for x in range(10) if x % 2 == 0]
print("Even Numbers:", evens)

# Nested List Comprehension - Flattening a matrix (list of lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened Matrix:", flattened)

# Conditional Expressions in List Comprehensions - Creating a list of 'Even'/'Odd' labels
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]
print("Labels:", labels)

# List Comprehension with Multiple Iterables - Creating a list of concatenated pairs
colors = ["red", "green", "blue"]
fruits = ["apple", "banana", "cherry"]
combined = [color + "_" + fruit for color in colors for fruit in fruits]
print("Combined Color and Fruit Names:", combined)

# Using List Comprehension with Functions
def square(x):
    return x * x

squared_numbers = [square(x) for x in range(10)]
print("Squared Numbers (Using Function):", squared_numbers)
