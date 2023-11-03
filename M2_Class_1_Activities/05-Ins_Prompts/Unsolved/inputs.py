# Collect the user's input for the prompt "What is your name?"
user_name = input("What is your name?")

# Print the data type of user_name
print("Data type of user_name:", type(user_name))

# Collect the user's input for the prompt "How old are you?" and convert the
# string to an integer.
age = int(input("How old are you?"))

# Print the data type of age
print("Data type of age:", type(age))

# Collect the user's input for the prompt "What is your average weekly grocery 
# bill?" and convert the string to a float.
grocery_bill = float(input("What is your average weekly grocery bill?"))

# Print the data type of grocery_bill
print("Data type of grocery_bill:", type(grocery_bill))

# Collect the user's input for the prompt "Will you type an input?" and
# convert it to a boolean. Note that non-zero, non-empty objects return True.
true_or_false = bool(input("Will you type an input?"))

# Print the data type of true_or_false
print("Data type of true_or_false:", type(true_or_false))

# Create four print statements that display text about the user's inputs.
print("Hello,", user_name)
print("You are", age, "years old.")
print("Your average weekly grocery bill is $", grocery_bill)
if true_or_false:
    print("You are willing to type an input.")
else:
    print("You are not willing to type an input.")
