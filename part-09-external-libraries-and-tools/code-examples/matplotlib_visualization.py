# matplotlib_visualization.py
import matplotlib.pyplot as plt
import numpy as np

# Simple Line Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('Simple Line Plot')
plt.xlabel('x axis')
plt.ylabel('sin(x)')
plt.show()

# Scatter Plot
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.title('Simple Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Bar Graph
categories = ['Category A', 'Category B', 'Category C']
values = [10, 20, 15]
plt.bar(categories, values)
plt.title('Simple Bar Graph')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# Histogram
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.title('Simple Histogram')
plt.xlabel('Data')
plt.ylabel('Frequency')
plt.show()

# Example usage
print("Matplotlib Visualization Demonstration Completed.")
