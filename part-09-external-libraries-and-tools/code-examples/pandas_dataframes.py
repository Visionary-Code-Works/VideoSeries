# pandas_dataframes.py
import pandas as pd

# Creating a DataFrame from a Dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("DataFrame from Dictionary:\n", df)

# Selecting Columns
print("\nName Column:\n", df['Name'])

# Adding a New Column
df['Salary'] = [70000, 80000, 90000]
print("\nDataFrame with Salary Column:\n", df)

# Deleting a Column
df.drop('Age', axis=1, inplace=True)
print("\nDataFrame after dropping Age column:\n", df)

# Filtering Rows
filtered_df = df[df['Salary'] > 75000]
print("\nRows with Salary greater than 75000:\n", filtered_df)

# Reading Data from a CSV File (Example)
# df_from_csv = pd.read_csv('path_to_csv_file.csv')

# Writing DataFrame to a CSV File
# df.to_csv('path_to_output_csv_file.csv', index=False)

# Example usage
print("\nPandas DataFrame Demonstration Completed.")
