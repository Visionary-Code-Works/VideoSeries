# PracticalPythonExercises.py

# Exercise 1: File Processing
# Read a text file and print each line with its line number.
filename = 'sample.txt'  # Replace with a valid filename
try:
    with open(filename, 'r') as file:
        for i, line in enumerate(file, start=1):
            print(f"{i}: {line.strip()}")
except FileNotFoundError:
    print(f"File {filename} not found.")

# Exercise 2: Data Parsing
# Parse a CSV file and calculate the average of a numeric column.
import csv

csv_file = 'data.csv'  # Replace with a valid CSV file path
try:
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        total, count = 0, 0
        for row in reader:
            total += float(row['columnName'])  # Replace 'columnName' with the column name
            count += 1
        average = total / count if count > 0 else 0
        print(f"Average: {average}")
except FileNotFoundError:
    print(f"CSV file {csv_file} not found.")

# Exercise 3: Web Scraping
# Use Beautiful Soup to scrape the title of a webpage.
from bs4 import BeautifulSoup
import requests

url = 'https://www.example.com'  # Replace with a valid URL
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
title = soup.title.text if soup.title else 'No title found'
print(f"Title of the webpage: {title}")

# Exercise 4: API Request
# Make a GET request to a public API and print part of the response data.
api_url = 'https://api.example.com/data'  # Replace with a valid API URL
response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
    print(data[:5])  # Print the first 5 items of the data
else:
    print("Failed to retrieve data")

# Exercise 5: Data Visualization
# Create a simple plot of a list of values using Matplotlib.
from matplotlib import pyplot as plt

values = [5, 3, 7, 2, 4, 6]
plt.plot(values)
plt.title('Sample Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
