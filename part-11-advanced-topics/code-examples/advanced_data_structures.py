""" advanced_data_structures.py
_summary_

_extended_summary_

- `namedtuple_example` demonstrates how to create and use namedtuples, which are extensions of tuples that allow for more readable code by accessing elements by name.
- `defaultdict_example` shows how to use a defaultdict, a dictionary-like object that provides a default value for a nonexistent key.
- `counter_example` illustrates the use of Counter, a dictionary subclass for counting hashable objects.

This example file demonstrates how these advanced data structures from Python's collections module can be used to write more efficient and readable code for various applications.
"""


from collections import namedtuple, defaultdict, Counter

def namedtuple_example():
    """ Demonstrates the use of namedtuple """
    # Creating a namedtuple
    Person = namedtuple('Person', 'name age city')

    # Creating instances of Person
    alice = Person(name="Alice", age=30, city="New York")
    bob = Person(name="Bob", age=25, city="Paris")

    # Accessing fields
    print(f"{alice.name} is {alice.age} years old and lives in {alice.city}")
    print(f"{bob.name} is {bob.age} years old and lives in {bob.city}")

def defaultdict_example():
    """ Demonstrates the use of defaultdict """
    # Creating a defaultdict with default type list
    fruits_by_color = defaultdict(list)

    # Adding items to the defaultdict
    fruits_by_color['yellow'].append('banana')
    fruits_by_color['green'].append('apple')
    fruits_by_color['red'].append('cherry')

    # Printing the defaultdict
    for color, fruits in fruits_by_color.items():
        print(f"{color}: {fruits}")

def counter_example():
    """ Demonstrates the use of Counter """
    # Creating a Counter to count occurrences of elements in a list
    colors = ['blue', 'red', 'blue', 'green', 'red', 'blue']
    color_count = Counter(colors)

    # Printing the count of each element
    for color, count in color_count.items():
        print(f"{color}: {count}")

def main():
    print("Namedtuple Example:")
    namedtuple_example()

    print("\nDefaultdict Example:")
    defaultdict_example()

    print("\nCounter Example:")
    counter_example()

if __name__ == "__main__":
    main()
