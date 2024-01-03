# with_statement_file_handling.py

# Reading from a file using 'with' statement
def read_with_statement(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print("Reading with 'with' statement:\n", content)

# Writing to a file using 'with' statement
def write_with_statement(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)
        print("Writing done with 'with' statement.")

# Example usage
file_path = 'example.txt'
write_with_statement(file_path, "This file was written using the 'with' statement.\n")
read_with_statement(file_path)
