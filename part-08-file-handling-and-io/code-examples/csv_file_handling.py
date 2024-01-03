# csv_file_handling.py
import csv

# Reading a CSV File
def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Writing to a CSV File
def write_csv_file(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

# Example usage
csv_read_path = 'example_read.csv'
csv_write_path = 'example_write.csv'
sample_data = [['Name', 'Age'], ['Alice', 24], ['Bob', 19]]

write_csv_file(csv_write_path, sample_data)
print("CSV Writing Complete.\nReading the written CSV:")
read_csv_file(csv_write_path)
