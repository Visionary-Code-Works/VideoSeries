# custom_exceptions.py

# Defining a custom exception class
class MyCustomError(Exception):
    """Exception raised for custom purposes.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message

# Using the custom exception
try:
    raise MyCustomError("Something went wrong!")
except MyCustomError as e:
    print(f"Caught MyCustomError: {e.message}")

# Example with additional functionality
class ValidationError(Exception):
    """Exception raised when a validation fails.

    Attributes:
        field -- field in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, field, message="Invalid input"):
        self.field = field
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.field}: {self.message}"

# Raising the ValidationError
try:
    raise ValidationError("Email", "Invalid email format")
except ValidationError as e:
    print(e)

# The script shows how to create custom exception classes and use them to handle specific error conditions.
# Custom exceptions make error handling more clear and maintainable, especially in larger applications.
