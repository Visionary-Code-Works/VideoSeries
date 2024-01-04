""" decorators_examples.py
_summary_

_extended_summary_

Returns:
    _type_: _description_

- `simple_decorator` is a basic decorator that adds functionality (printing messages) before and after a function call.
- `say_hello` is a simple function that gets decorated by `simple_decorator`.
- `repeat` is a more complex decorator that takes an argument and repeats the execution of the decorated function a specified number of times.
- `greet` is a function that takes a name as an argument and is decorated with `repeat` to call it multiple times.
"""


def simple_decorator(function):
    """ A simple decorator function that prints a message before and after the function call. """
    def wrapper():
        print("Something is happening before the function is called.")
        function()
        print("Something is happening after the function is called.")
    return wrapper

@simple_decorator
def say_hello():
    """ A simple function to demonstrate decoration """
    print("Hello!")

def repeat(times):
    """ Decorator to repeat a function call 'times' times. """
    def decorator_repeat(function):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                function(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(times=3)
def greet(name):
    """ Function to greet a person """
    print(f"Hello {name}!")

def main():
    say_hello()  # Calling the decorated function
    greet("Alice")  # Calling the decorated function with arguments

if __name__ == "__main__":
    main()
