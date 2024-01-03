# finally_usage.py

# Example of using a try-except-finally block
try:
    # Attempting a division operation that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero error occurred.")
finally:
    print("This is the finally block, executing after the try-except.")

# Example with file handling
try:
    file = open("example.txt", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found.")
finally:
    # Ensuring the file is closed even if an error occurs
    file.close()
    print("File has been closed.")

# The script demonstrates the use of the finally block to ensure that certain actions are taken,
# such as closing a file, regardless of whether an exception occurs.
