# DataStructuresExercises.py

# Exercise 1: List Operations
# Create a list of numbers from 1 to 5, then append 6 to the list and print it
numbers_list = [1, 2, 3, 4, 5]
numbers_list.append(6)
print("Exercise 1:", numbers_list)

# Exercise 2: List Slicing
# Given the list, slice it to get a new list containing elements from index 2 to 4
sample_list = [10, 20, 30, 40, 50, 60]
sliced_list = sample_list[2:5]
print("Exercise 2:", sliced_list)

# Exercise 3: Tuple Creation
# Create a tuple with different data types (int, string, float) and print it
mixed_tuple = (1, "Python", 3.14)
print("Exercise 3:", mixed_tuple)

# Exercise 4: Access Tuple Elements
# Given the tuple, access and print the second element
sample_tuple = ("apple", "banana", "cherry")
print("Exercise 4:", sample_tuple[1])

# Exercise 5: Set Manipulation
# Create a set, add an element to it, then remove a different element
fruit_set = {"apple", "banana", "cherry"}
fruit_set.add("orange")
fruit_set.discard("banana")
print("Exercise 5:", fruit_set)

# Exercise 6: Dictionary Operations
# Create a dictionary representing a person (name, age, city), then change the age
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
person["age"] = 30
print("Exercise 6:", person)

# Exercise 7: Working with Dictionary Items
# Given the dictionary, iterate over it and print keys and values
sample_dict = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}
print("Exercise 7:")
for color, hex_code in sample_dict.items():
    print(f"{color}: {hex_code}")

# Exercise 8: Nested Data Structures
# Create a nested dictionary or list and access elements in it
nested_dict = {
    "fruit": "apple",
    "details": {"color": "red", "taste": "sweet"}
}
print("Exercise 8:", nested_dict["details"]["color"])

# Exercise 9: List Comprehension
# Use list comprehension to create a list of squares for numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]
print("Exercise 9:", squares)

# Exercise 10: Set Union and Intersection
# Given two sets, print their union and intersection
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Exercise 10: Union -", set1.union(set2), "Intersection -", set1.intersection(set2))
