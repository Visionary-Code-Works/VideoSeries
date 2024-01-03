# if_else_examples.py

# Basic if-else statement
age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Using elif for multiple conditions
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or F")

# Nested if-else
num = 15
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

# Short Hand If - Single Line
temperature = 30
if temperature > 25: print("It's a hot day.")

# Short Hand If-Else - Single Line (Ternary Operator)
is_raining = True
activity = "Stay inside" if is_raining else "Go outside"
print(activity)

# Checking multiple conditions with logical operators
username = "admin"
password = "secret"
if username == "admin" and password == "secret":
    print("Access granted")
else:
    print("Access denied")

# End of if_else_examples.py
