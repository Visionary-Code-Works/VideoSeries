# dictionary_advanced.py

# Creating a basic dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}

# Dictionary Comprehension - Squaring numbers
squares = {x: x*x for x in range(6)}
print("Squares:", squares)

# Inverting a dictionary (swap keys and values)
inverted_person = {value: key for key, value in person.items()}
print("Inverted Person Dictionary:", inverted_person)

# Filtering items in a dictionary
filtered_person = {key: value for key, value in person.items() if key != "age"}
print("Filtered Person Dictionary (without age):", filtered_person)

# Merging two dictionaries using dictionary comprehension and unpacking
additional_info = {"occupation": "Engineer", "hobbies": ["Reading", "Traveling"]}
merged_dict = {**person, **additional_info}
print("Merged Dictionary:", merged_dict)

# Dictionary Comprehension with Conditional Logic
parity = {x: ("even" if x % 2 == 0 else "odd") for x in range(6)}
print("Numbers and their Parity:", parity)

# Nested Dictionary Comprehension
nested_dict = {x: {y: x*y for y in range(1, 4)} for x in range(1, 4)}
print("Nested Dictionary (Multiplication Table):", nested_dict)

# Using dictionary comprehension to create a dictionary from two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined_dict = {keys[i]: values[i] for i in range(len(keys))}
print("Dictionary from two lists:", combined_dict)

# End of dictionary_advanced.py
