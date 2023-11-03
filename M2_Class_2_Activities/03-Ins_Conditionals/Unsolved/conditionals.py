# Get user input for variables
x = input("Enter the value for variable 'x': ")
y = input("Enter the value for variable 'y': ")

# Check if one value is equal to another
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")

# Check if one value is NOT equal to another
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# Check if one value is less than another
if x < y:
    print("x is less than y")
else:
    print("x is not less than y")

# Check if one value is greater than another
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# Check if a value is greater than or equal to another
if x >= y:
    print("x is greater than or equal to y")
else:
    print("x is less than y")

# Use a Boolean to check a condition
# Get user input for is_sunny
user_input = input("Is it a sunny day? (yes/no): ")

# Check if it's a sunny day based on user input
if user_input.lower() == "yes":
    is_sunny = True
    print("It's a sunny day!")
else:
    is_sunny = False
    print("It's not a sunny day.")

# Get user input and check if it's a number
user_input = input("Enter a number: ")

if user_input.isdigit():
    print(f"You entered a number: {user_input}")
else:
    print(f"You did not enter a number: {user_input}")
