""" generators_and_iterators.py
_summary_

_extended_summary_

Raises:
    StopIteration: _description_

Returns:
    _type_: _description_

Yields:
    _type_: _description_

- `countdown` is a generator function that yields a countdown from the given number down to 1.
- `fibonacci` is another generator function that yields the Fibonacci sequence up to a specified limit.
- `SquareIterator` is an iterator class that implements `__iter__` and `__next__` to return the squares of numbers up to a given limit.
"""

def countdown(num):
    """ Generator function that counts down from a given number """
    print(f"Starting countdown from {num}")
    while num > 0:
        yield num
        num -= 1

def fibonacci(limit):
    """ Generator function for Fibonacci sequence up to a limit """
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

class SquareIterator:
    """ Iterator class that returns the squares of numbers up to a limit """
    def __init__(self, limit):
        self.limit = limit
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num >= self.limit:
            raise StopIteration
        result = self.num ** 2
        self.num += 1
        return result

def main():
    # Using the countdown generator
    for number in countdown(5):
        print(number)

    print("\nFibonacci sequence:")
    # Using the Fibonacci generator
    for number in fibonacci(10):
        print(number)

    print("\nSquares up to a limit:")
    # Using the SquareIterator
    squares = SquareIterator(5)
    for square in squares:
        print(square)

if __name__ == "__main__":
    main()
