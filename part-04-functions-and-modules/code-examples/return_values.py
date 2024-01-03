# return_values.py

# Function returning a simple value
def square(number):
    return number * number

result = square(4)
print(f"The square of 4 is {result}")

# Function returning a tuple
def get_coordinates():
    x_coordinate = 10
    y_coordinate = 20
    return (x_coordinate, y_coordinate)

x, y = get_coordinates()
print(f"Coordinates are: x={x}, y={y}")

# Function returning a list
def get_even_numbers(max_number):
    even_numbers = [num for num in range(max_number) if num % 2 == 0]
    return even_numbers

evens = get_even_numbers(10)
print(f"Even numbers up to 10: {evens}")

# Function returning a dictionary
def create_user(username, age):
    user = {"username": username, "age": age}
    return user

user_info = create_user("john_doe", 30)
print(f"User info: {user_info}")

# Function returning multiple values
def min_max(numbers):
    return min(numbers), max(numbers)

min_num, max_num = min_max([1, 2, 3, 4, 5])
print(f"Minimum: {min_num}, Maximum: {max_num}")

# End of return_values.py
