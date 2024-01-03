# dictionary_usage.py

# Creating a Dictionary
person = {
    "name": "John Doe",
    "age": 30,
    "occupation": "Software Engineer"
}
print("Original Dictionary:", person)

# Accessing Elements
print("\nName:", person["name"])
print("Age:", person.get("age"))

# Adding Elements
person["city"] = "New York"
print("\nAfter adding city:", person)

# Updating Elements
person["age"] = 31
print("\nAfter updating age:", person)

# Removing Elements
del person["occupation"]  # Removes the key-value pair for 'occupation'
print("\nAfter removing occupation:", person)

# Using pop() method
city = person.pop("city")  # Removes 'city' and returns its value
print(f"Removed city: {city}")
print("After popping city:", person)

# Iterating through a Dictionary
print("\nIterating through the dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary Comprehensions
squares = {x: x*x for x in range(1, 6)}
print("\nDictionary Comprehensions (squares):", squares)

# Nested Dictionaries
people = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 28}
}
print("\nNested Dictionary (people):", people)

# Accessing Elements in Nested Dictionary
print("\nName of person1:", people["person1"]["name"])

# All Keys and Values
print("\nAll keys:", person.keys())
print("All values:", person.values())
