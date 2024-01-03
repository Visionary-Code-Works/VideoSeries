# for_loop_examples.py

# Iterating over a range
print("For Loop with Range:")
for i in range(5):
    print(i)

# Iterating over a list
print("\nFor Loop with List:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using enumerate for indexes and elements
print("\nFor Loop with enumerate:")
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# Iterating over a string
print("\nFor Loop with String:")
for char in "Python":
    print(char)

# Loop with range and step
print("\nFor Loop with Range and Step:")
for i in range(0, 10, 2):  # Start at 0, up to (but not including) 10, step by 2
    print(i)

# Nested for loops
print("\nNested For Loops:")
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")

# Using break to exit a loop
print("\nFor Loop with break:")
for num in range(5):
    if num == 3:
        break
    print(num)

# Using continue to skip the current iteration
print("\nFor Loop with continue:")
for num in range(5):
    if num == 3:
        continue
    print(num)

# Using else with for loops
print("\nFor Loop with else:")
for num in range(3):
    print(num)
else:
    print("Loop is finished")

# Using list comprehension
print("\nList Comprehension:")
squares = [x * x for x in range(5)]
print(squares)

# End of for_loop_examples.py
