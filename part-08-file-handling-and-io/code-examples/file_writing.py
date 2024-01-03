# file_writing.py

# Writing to a File
def write_to_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)

# Appending to a File
def append_to_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write(text)

# Writing a List to a File
def write_list_to_file(file_path, list_content):
    with open(file_path, 'w') as file:
        for item in list_content:
            file.write(f"{item}\n")

# Example usage
file_path = 'example.txt'
write_to_file(file_path, "Hello, Python!\n")
append_to_file(file_path, "Appending a new line.\n")
write_list_to_file(file_path, ["Line 1", "Line 2", "Line 3"])
