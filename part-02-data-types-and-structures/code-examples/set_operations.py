# set_operations.py

# Creating a Set
fruits = {"apple", "banana", "cherry"}
print("Original Set:", fruits)

# Adding Elements
fruits.add("orange")
print("\nAfter Adding 'orange':", fruits)

# Removing Elements
fruits.remove("banana")  # Removing 'banana' from the set
print("\nAfter Removing 'banana':", fruits)

# Using discard() to Remove Elements
fruits.discard("pineapple")  # Discarding an element not present doesn't raise an error
print("\nAfter Discarding 'pineapple':", fruits)

# Checking Membership
print("\nIs 'apple' in fruits?", "apple" in fruits)

# Union of Sets
vegetables = {"carrot", "potato", "cucumber"}
all_items = fruits.union(vegetables)
print("\nUnion of Fruits and Vegetables:", all_items)

# Intersection of Sets
some_fruits = {"apple", "kiwi", "orange"}
common_fruits = fruits.intersection(some_fruits)
print("\nCommon Fruits:", common_fruits)

# Difference of Sets
unique_fruits = fruits.difference(some_fruits)
print("\nUnique Fruits in 'fruits' set:", unique_fruits)

# Symmetric Difference
sym_diff_fruits = fruits.symmetric_difference(some_fruits)
print("\nSymmetric Difference:", sym_diff_fruits)

# Iterating through a Set
print("\nIterating through the set:")
for fruit in fruits:
    print(fruit)

# Set Comprehension
squared_numbers = {x * x for x in range(1, 6)}
print("\nSquared Numbers (Set Comprehension):", squared_numbers)

# Converting List to Set
fruit_list = ["apple", "banana", "cherry", "apple"]
fruit_set = set(fruit_list)
print("\nConverted Set from List:", fruit_set)
