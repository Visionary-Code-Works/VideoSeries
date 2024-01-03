# modules_usage.py

import math
from datetime import datetime
import random
import os

# Using the math module
def calculate_circle_area(radius):
    return math.pi * radius ** 2

radius = 5
area = calculate_circle_area(radius)
print(f"The area of a circle with radius {radius} is {area:.2f}")

# Using the datetime module
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current datetime is: {formatted_time}")

# Using the random module
random_number = random.randint(1, 100)
print(f"A random number between 1 and 100: {random_number}")

# Generating a random choice
fruits = ["Apple", "Banana", "Cherry"]
chosen_fruit = random.choice(fruits)
print(f"A random fruit choice: {chosen_fruit}")

# Using the os module
current_directory = os.getcwd()
print(f"The current working directory is: {current_directory}")

# List files in a directory
print("Files in current directory:")
for file in os.listdir(current_directory):
    print(file)

# End of modules_usage.py
