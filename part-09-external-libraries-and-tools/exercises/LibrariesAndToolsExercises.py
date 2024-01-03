# LibrariesAndToolsExercises.py

# Before starting, make sure to install the required libraries:
# pip install pandas requests matplotlib beautifulsoup4

import pandas as pd
import requests
from matplotlib import pyplot as plt
from bs4 import BeautifulSoup

# Exercise 1: Pandas - Data Manipulation
# Read a CSV file into a Pandas DataFrame and display the first 5 rows.
df = pd.read_csv('example.csv')  # Replace 'example.csv' with a valid CSV file path
print("First 5 rows of the DataFrame:")
print(df.head())

# Exercise 2: Requests - HTTP Requests
# Use the Requests library to make a GET request to an API and print the status code.
response = requests.get('https://api.example.com/data')  # Replace with a valid API URL
print("Status Code:", response.status_code)

# Exercise 3: Matplotlib - Basic Plotting
# Create a simple line plot of a Pandas DataFrame column.
plt.plot(df['column_name'])  # Replace 'column_name' with a valid column name
plt.title('Line Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()

# Exercise 4: Beautiful Soup - Web Scraping
# Scrape the title of a webpage using Beautiful Soup.
url = 'https://www.example.com'  # Replace with a valid URL
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text
print("Webpage Title:", title)

# Exercise 5: Combining Libraries
# Fetch data from an API, load it into a DataFrame, and plot it.
api_response = requests.get('https://api.example.com/data')  # Replace with a valid API URL
api_data = api_response.json()
api_df = pd.DataFrame(api_data)
api_df.plot()  # Customize the plot as needed
plt.show()

# End of LibrariesAndToolsExercises.py
