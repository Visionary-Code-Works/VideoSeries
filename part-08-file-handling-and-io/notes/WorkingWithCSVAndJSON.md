# WorkingWithCSVAndJSON.md

## Handling CSV and JSON Files in Python

CSV (Comma Separated Values) and JSON (JavaScript Object Notation) are two common file formats used in data exchange and storage. Python provides robust support for both CSV and JSON file handling.

---

**1. Working with CSV Files**

- **Reading CSV**: Using the `csv.reader` or `pandas.read_csv()`.
- **Writing CSV**: Using the `csv.writer` or `pandas.DataFrame.to_csv()`.
- **Example**:

     ```python
     import csv
     with open('file.csv', 'r') as file:
         reader = csv.reader(file)
         for row in reader:
             print(row)
     ```

**2. Handling JSON Files**

- **Parsing JSON**: Using the `json` module to parse JSON strings and files.
- **Serializing to JSON**: Converting Python objects to JSON format using `json.dumps()` or `json.dump()`.
- **Example**:

     ```python
     import json
     with open('file.json', 'r') as file:
         data = json.load(file)
         print(data)
     ```

**3. Practical Applications**

- CSV files are commonly used in data analysis, machine learning, and database migration.
- JSON is widely used in web APIs, configuration files, and NoSQL databases.
