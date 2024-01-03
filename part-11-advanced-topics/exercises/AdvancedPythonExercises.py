# AdvancedPythonExercises.py

# Exercise 1: Decorators
# Write a decorator that prints the execution time of a function.
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start} seconds")
        return result
    return wrapper

@timing_decorator
def example_function(n):
    return sum(range(n))

print(example_function(1000000))

# Exercise 2: Generators
# Create a generator function that yields the square of numbers up to a given number.
def square_generator(limit):
    for i in range(limit):
        yield i * i

for val in square_generator(5):
    print(val)

# Exercise 3: Comprehensions
# Use a dictionary comprehension to create a dictionary where keys are numbers from 1 to 5 and values are their cubes.
cubes = {x: x**3 for x in range(1, 6)}
print(cubes)

# Exercise 4: Lambda Functions
# Create a lambda function that takes two arguments and returns their product.
product = lambda x, y: x * y
print(product(5, 3))

# Exercise 5: Map and Filter
# Use `map` and `filter` to convert temperatures in Celsius to Fahrenheit and filter out temperatures below freezing.
celsius = [0, 10, 20, -7, 25]
fahrenheit = list(map(lambda x: (x * 9/5) + 32, filter(lambda x: x > 0, celsius)))
print(fahrenheit)

# Exercise 6: Working with Asyncio
# Write an async function that simulates a small task and use asyncio to run it.
import asyncio

async def async_task():
    print("Starting task")
    await asyncio.sleep(1)
    print("Finished task")

asyncio.run(async_task())

# End of AdvancedPythonExercises.py
