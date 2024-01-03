# context_managers.py

# Using a context manager for file operations
def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

# Reading a file using the context manager
try:
    content = read_file('example.txt')
    print(content)
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading file.")

# Creating a custom context manager
from contextlib import contextmanager

@contextmanager
def custom_open(file_name):
    try:
        file = open(file_name, 'r')
        yield file
    finally:
        file.close()

# Using the custom context manager
try:
    with custom_open('example.txt') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading file.")

# This script provides examples of using built-in and custom context managers for safe and clean handling of external resources.
