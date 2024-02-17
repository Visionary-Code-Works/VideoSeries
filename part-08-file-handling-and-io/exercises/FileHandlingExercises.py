# FileHandlingExercises.py

# Exercise 1: Reading from a File
# Read the contents of a file named "example.txt" and print them to the console.
try:
    with open('example.txt', mode='r', encoding='utf-8') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("The file does not exist.")

# Exercise 2: Writing to a File
# Write a string "Hello, Python!" to a file named "output.txt".
with open('output.txt', mode='w', encoding='utf-8') as file:
    file.write("Hello, Python!")

# Exercise 3: Appending to a File
# Append "This is a new line." to the file named "output.txt".
with open('output.txt', mode='a', encoding='utf-8') as file:
    file.write("\nThis is a new line.")

# Exercise 4: Reading Line by Line
# Read "example.txt" line by line and print each line with its line number.
try:
    with open('example.txt', mode='r', encoding='utf-8') as file:
        line_number = 1
        for line in file:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1
except FileNotFoundError:
    print("The file does not exist.")

# Exercise 5: Working with Multiple Files
# Copy the contents of "example.txt" to a new file "copy.txt".
try:
    with open('example.txt', mode='r', encoding='utf-8') as source_file:
        with open('copy.txt', mode='w', encoding='utf-8') as dest_file:
            for line in source_file:
                dest_file.write(line)
except FileNotFoundError:
    print("The source file does not exist.")

# Exercise 6: Using Different File Modes
# Use the 'r+' mode to read and append text to "example.txt".
try:
    with open('example.txt', mode='r+', encoding='utf-8') as file:
        original_content = file.read()
        file.write("\nText to append.")
        file.seek(0)
        updated_content = file.read()
        print("Original Content:")
        print(original_content)
        print("\nUpdated Content:")
        print(updated_content)
except FileNotFoundError:
    print("The file does not exist.")

# End of FileHandlingExercises.py
