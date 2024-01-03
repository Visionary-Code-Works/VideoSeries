# basic_exception_handling.py

# Example 1: Handling a ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Attempted to divide by zero.")
else:
    print(f"Division result is {result}")

# Example 2: Handling multiple exceptions
try:
    list = [1, 2, 3]
    print(list[3])
except IndexError:
    print("Index is out of range.")
except Exception as e:
    print(f"An error occurred: {e}")

# Example 3: Generic exception catch-all
try:
    undefined_variable
except NameError:
    print("A NameError occurred.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Example 4: Handling and re-raising an exception
try:
    if 'condition':
        raise ValueError("A custom error message")
except ValueError as ve:
    print(f"Caught an exception: {ve}")
    raise  # Re-raise the exception

# The script demonstrates various ways to handle exceptions using try-except blocks.
# It includes handling specific exceptions, catching all exceptions, and re-raising an exception.
