# AdvancedDataStructuresExercises.py

# Exercise 1: List Comprehension
# Use list comprehension to create a list of squares for numbers from 1 to 10.
squares = [x*x for x in range(1, 11)]
print("Squares from 1 to 10:", squares)

# Exercise 2: Set Operations
# Given two sets, perform union and intersection operations.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
print("Union:", union_set)
print("Intersection:", intersection_set)

# Exercise 3: Dictionary Comprehension
# Create a dictionary where keys are numbers from 1 to 5 and values are their cubes using dictionary comprehension.
cubes = {x: x**3 for x in range(1, 6)}
print("Cubes:", cubes)

# Exercise 4: Nested Dictionaries
# Create a nested dictionary to store data of students (name and age).
students = {
    'Alice': {'age': 22, 'major': 'Biology'},
    'Bob': {'age': 23, 'major': 'Chemistry'}
}
print("Students:", students)

# Exercise 5: Set Comprehension
# Use set comprehension to create a set of even numbers from 1 to 10.
evens = {x for x in range(1, 11) if x % 2 == 0}
print("Even numbers from 1 to 10:", evens)

# Exercise 6: Working with Nested Data Structures
# Access and print the major of each student from the 'students' nested dictionary.
print("Students' Majors:")
for name, details in students.items():
    print(f"{name}: {details['major']}")

# Exercise 7: Dictionary Manipulation
# Update the age of one student and add another student to the 'students' dictionary.
students['Alice']['age'] = 23
students['Charlie'] = {'age': 21, 'major': 'Physics'}
print("Updated Students:", students)

# End of AdvancedDataStructuresExercises.py
