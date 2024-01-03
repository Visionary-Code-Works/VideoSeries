# list_operations.py

# Creating a List
numbers = [1, 2, 3, 4, 5]
print("Original List:", numbers)

# Accessing Elements
print("\nFirst Element:", numbers[0])
print("Last Element:", numbers[-1])

# Adding Elements
numbers.append(6)  # Appending to the end of the list
print("\nAfter Appending 6:", numbers)

numbers.insert(0, 0)  # Inserting at the beginning of the list
print("After Inserting 0 at the beginning:", numbers)

# Removing Elements
numbers.remove(3)  # Removing the first occurrence of 3
print("\nAfter Removing 3:", numbers)

popped_element = numbers.pop()  # Popping the last element
print("Popped Element:", popped_element)
print("After Popping an element:", numbers)

# Slicing Lists
sub_list = numbers[1:4]  # Getting a slice of the list
print("\nSub List (1 to 4):", sub_list)

# List Comprehension
squared_numbers = [x * x for x in numbers]
print("\nSquared Numbers:", squared_numbers)

# Iterating through a List
print("\nIterating through the list:")
for num in numbers:
    print(num)

# Sorting Lists
numbers.sort()  # Sorting the list in place
print("\nSorted List:", numbers)

# Reversing Lists
numbers.reverse()  # Reversing the list in place
print("Reversed List:", numbers)

# Concatenating Lists
additional_numbers = [7, 8, 9]
combined_list = numbers + additional_numbers
print("\nCombined List:", combined_list)

# Finding the Length of a List
length = len(numbers)
print("\nLength of the List:", length)
