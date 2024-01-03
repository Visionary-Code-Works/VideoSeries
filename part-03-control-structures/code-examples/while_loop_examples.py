# while_loop_examples.py

# Basic while loop
print("Basic While Loop:")
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# While loop with a break statement
print("\nWhile Loop with Break:")
counter = 0
while True:
    if counter >= 5:
        break
    print(counter)
    counter += 1

# While loop with a continue statement
print("\nWhile Loop with Continue:")
counter = 0
while counter < 5:
    counter += 1
    if counter == 3:
        continue
    print(counter)

# While loop with an else clause
print("\nWhile Loop with Else:")
counter = 0
while counter < 3:
    print(counter)
    counter += 1
else:
    print("Counter is no longer less than 3")

# Infinite loop (Uncomment to run)
# print("\nInfinite While Loop:")
# while True:
#     print("This will run forever!")

# Nested while loops
print("\nNested While Loops:")
outer_counter = 0
while outer_counter < 3:
    inner_counter = 0
    while inner_counter < 2:
        print(f"Outer: {outer_counter}, Inner: {inner_counter}")
        inner_counter += 1
    outer_counter += 1

# Using while loop to iterate through a list
print("\nWhile Loop with List Iteration:")
fruits = ["apple", "banana", "cherry"]
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1

# End of while_loop_examples.py
