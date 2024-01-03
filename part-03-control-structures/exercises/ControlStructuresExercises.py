# ControlStructuresExercises.py

# Exercise 1: If-Else
# Ask the user to input a number. If the number is greater than 10, print "Greater than 10." Otherwise, print "Less than or equal to 10."
number = int(input("Enter a number: "))
if number > 10:
    print("Greater than 10.")
else:
    print("Less than or equal to 10.")

# Exercise 2: For Loop
# Use a for loop to print all even numbers from 1 to 20.
print("Even numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Exercise 3: Nested If-Else
# Ask the user for their age. If the age is greater than 18, check if it's even or odd and print a message accordingly. If the age is less than 18, print "Underage."
age = int(input("Enter your age: "))
if age > 18:
    if age % 2 == 0:
        print("You are an adult with an even age.")
    else:
        print("You are an adult with an odd age.")
else:
    print("Underage.")

# Exercise 4: While Loop
# Write a while loop that starts at 10 and counts down to 1 (inclusive), printing each number.
print("Countdown:")
count = 10
while count >= 1:
    print(count)
    count -= 1

# Exercise 5: Loop with Break
# Write a for loop that iterates over numbers from 1 to 10 and breaks the loop when it reaches 5, then prints "Loop stopped."
for i in range(1, 11):
    if i == 5:
        print("Loop stopped.")
        break

# Exercise 6: Loop with Continue
# Write a for loop that iterates over numbers from 1 to 10 and uses continue to skip the number 5, printing each number.
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# End of ControlStructuresExercises.py
