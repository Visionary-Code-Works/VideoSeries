# data_types.py

# Integer
integer_example = 42
print("Integer:", integer_example)

# Float
float_example = 3.14159
print("Float:", float_example)

# String
string_example = "Hello, Python!"
print("String:", string_example)

# Boolean
boolean_true = True
boolean_false = False
print("Boolean True:", boolean_true)
print("Boolean False:", boolean_false)

# List
list_example = [1, 2, 3, 4, 5]
print("List:", list_example)

# Tuple
tuple_example = (1, "apple", 3.14)
print("Tuple:", tuple_example)

# Set
set_example = {"apple", "banana", "cherry"}
print("Set:", set_example)

# Dictionary
dictionary_example = {"name": "Alice", "age": 25, "city": "Wonderland"}
print("Dictionary:", dictionary_example)

# Demonstrating mutability
print("\nBefore modifying list:", list_example)
list_example[0] = 100
print("After modifying list:", list_example)

print("\nBefore modifying dictionary:", dictionary_example)
dictionary_example["age"] = 26
print("After modifying dictionary:", dictionary_example)

# Note: Tuples and sets are immutable and will throw an error if you try to change them
