# nested_loops.py

# Nested for loops
print("Nested For Loops Example:")
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"i = {i}, j = {j}")

# Using nested loops to create a pattern
print("\nPattern Using Nested Loops:")
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print("")

# Nested while loops
print("\nNested While Loops Example:")
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1

# Nested loops with list comprehension
print("\nNested Loops with List Comprehension:")
matrix = [[j for j in range(3)] for i in range(3)]
for row in matrix:
    print(row)

# Nested loops for accessing elements in a multi-dimensional list
print("\nAccessing Elements in a 2D List:")
two_d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in two_d_list:
    for element in row:
        print(element, end=" ")
    print("")

# End of nested_loops.py
