# string_manipulation.py

# Basic String Operations
greeting = "Hello"
name = "Alice"
combined = greeting + " " + name  # String Concatenation
print("Concatenated String:", combined)

# String Slicing
substring = greeting[1:4]  # Slicing from index 1 to 3
print("Sliced String:", substring)

# String Length
length = len(greeting)
print("Length of String:", length)

# String Formatting with f-strings
age = 30
introduction = f"My name is {name} and I am {age} years old."
print("Formatted String:", introduction)

# Upper and Lower Case
print("Upper Case:", greeting.upper())
print("Lower Case:", greeting.lower())

# Stripping Whitespace
message = "   Hello World!   "
print("Stripped String:", message.strip())  # Removes leading and trailing whitespaces

# Replacing Substrings
replaced_message = message.replace("World", "Python")
print("Replaced String:", replaced_message)

# Splitting Strings
words = message.split()  # Splitting by whitespace
print("Split Words:", words)

# Joining Strings
joined_message = ", ".join(words)
print("Joined String:", joined_message)

# Checking for Substrings
contains_hello = "Hello" in message
print("Contains 'Hello':", contains_hello)

# Reversing a String
reversed_string = greeting[::-1]
print("Reversed String:", reversed_string)

# Multiline Strings
multiline = """This is a
multiline string."""
print("Multiline String:", multiline)

# Raw Strings (useful for regex and file paths)
raw_string = r"C:\User\name"
print("Raw String:", raw_string)

# End of string_manipulation.py
