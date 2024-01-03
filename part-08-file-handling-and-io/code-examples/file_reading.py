# file_reading.py

# Reading an Entire File at Once
def read_entire_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print("File content:\n", content)

# Reading a File Line by Line
def read_file_line_by_line(file_path):
    with open(file_path, 'r') as file:
        print("File content line by line:")
        for line in file:
            print(line.strip())

# Example usage
file_path = 'example.txt'
read_entire_file(file_path)
read_file_line_by_line(file_path)
