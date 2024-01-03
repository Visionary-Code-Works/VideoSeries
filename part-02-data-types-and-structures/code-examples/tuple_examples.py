# tuple_examples.py

# Creating Tuples
basic_tuple = (1, 2, 3, 4, 5)
print("Basic Tuple:", basic_tuple)

mixed_tuple = ("apple", 10, 3.14, "Python")
print("Mixed Tuple:", mixed_tuple)

# Single Element Tuple
single_element_tuple = ("single",)  # Comma is necessary for single element
print("Single Element Tuple:", single_element_tuple)

# Accessing Elements
first_element = basic_tuple[0]
print("\nFirst Element:", first_element)

last_element = mixed_tuple[-1]
print("Last Element:", last_element)

# Slicing Tuples
sliced_tuple = basic_tuple[1:4]
print("\nSliced Tuple:", sliced_tuple)

# Tuple Length
tuple_length = len(mixed_tuple)
print("\nLength of Mixed Tuple:", tuple_length)

# Iterating through a Tuple
print("\nIterating through Mixed Tuple:")
for item in mixed_tuple:
    print(item)

# Nested Tuples
nested_tuple = ("parent", (1, 2, 3), ["a", "b", "c"])
print("\nNested Tuple:", nested_tuple)

# Tuple Unpacking
a, b, c = basic_tuple[0:3]
print("\nUnpacked Values:", a, b, c)

# Tuples are Immutable
# Uncommenting the following line will raise an error
# basic_tuple[0] = 100

# Concatenating Tuples
concatenated_tuple = basic_tuple + mixed_tuple
print("\nConcatenated Tuple:", concatenated_tuple)

# Checking for an Element in a Tuple
contains_apple = "apple" in mixed_tuple
print("\nContains 'apple':", contains_apple)

# Count and Index Methods
count_of_1 = basic_tuple.count(1)
print("\nCount of 1 in Basic Tuple:", count_of_1)

index_of_apple = mixed_tuple.index("apple")
print("Index of 'apple':", index_of_apple)

# End of tuple_examples.py
