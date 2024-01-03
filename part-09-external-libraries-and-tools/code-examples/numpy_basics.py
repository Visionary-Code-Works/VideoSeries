# numpy_basics.py
import numpy as np

# Creating NumPy Arrays
arr_from_list = np.array([1, 2, 3, 4, 5])
print("Array from list:", arr_from_list)

# Array of zeros and ones
zeros_array = np.zeros(5)
ones_array = np.ones(5)
print("Zeros Array:", zeros_array)
print("Ones Array:", ones_array)

# Array of a range of numbers
range_array = np.arange(10, 20)
print("Range Array:", range_array)

# 2D Array (Matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array (Matrix):\n", matrix)

# Basic Array Operations
sum_array = np.sum(arr_from_list)
mean_array = np.mean(arr_from_list)
print("Sum of Array:", sum_array)
print("Mean of Array:", mean_array)

# Reshaping Arrays
reshaped_matrix = matrix.reshape(3, 2)
print("Reshaped Matrix:\n", reshaped_matrix)

# Indexing and Slicing
print("Element at index 2:", arr_from_list[2])
print("Slice from index 1 to 4:", arr_from_list[1:5])

# Linear Algebra Operations
print("Matrix Transpose:\n", matrix.transpose())

# Example usage
print("\nNumPy Basics Demonstration Completed.")
