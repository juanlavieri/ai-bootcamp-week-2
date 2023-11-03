# Function to get user input
def get_user_input(prompt):
    return input(prompt)

# 1. Check for two conditions to be met using "and"
x = int(get_user_input("Enter a value for x: "))
y = int(get_user_input("Enter a value for y: "))
if x > 0 and y < 10:
    print("Both conditions are met.")
else:
    print("Conditions are not met.")

# 2. Check if either of two conditions is met using "or"
if x == 1 or y == 10:
    print("At least one condition is met.")
else:
    print("Neither condition is met.")

# 3. Check if a condition is not true
if not (x > 0):
    print("x is not greater than 0.")
else:
    print("x is greater than 0.")

# 4. Check multiple conditions
z = int(get_user_input("Enter a value for z: "))
if x > 0 and y < 10 and z == 5:
    print("All conditions are met.")
else:
    print("Not all conditions are met.")

# 5. Check if a variable is in a list
name = get_user_input("Enter a name: ")
group_one = ["Jorge", "Joon", "Susan"]
group_two = ["Gerald", "Paola", "Ryder"]
group_three = ["Farah", "Amidah", "Koen"]

if name in group_one:
    print(f"{name} is in group one.")
elif name in group_two:
    print(f"{name} is in group two.")
elif name in group_three:
    print(f"{name} is in group three.")
else:
    print(f"{name} is not in any group.")

# 6. Check if a variable is not in a list
country = get_user_input("Enter a country: ")
countries = ["Fiji", "Australia", "New Zealand", "Papua New Guinea", "Palau",
             "Solomon Islands", "Micronesia", "Vanuatu", "Samoa", "Kiribati",
             "Tonga", "Marshall Islands", "Tuvalu", "Nauru"]

if country not in countries:
    print(f"{country} is not in the list of countries.")
else:
    print(f"{country} is in the list of countries.")

# 7. Check if a variable is a list
variable_to_check = get_user_input("Enter a variable to check if it's a list: ")
if isinstance(variable_to_check, list):
    print(f"{variable_to_check} is a list.")
else:
    print(f"{variable_to_check} is not a list.")

# 8. Check if a variable is not a list
variable_to_check = get_user_input("Enter a variable to check if it's not a list: ")
if not isinstance(variable_to_check, list):
    print(f"{variable_to_check} is not a list.")
else:
    print(f"{variable_to_check} is a list.")

# 9. Check if a variable is a float or integer
variable_to_check = float(get_user_input("Enter a variable to check if it's a float or integer: "))
if isinstance(variable_to_check, (int, float)):
    print(f"{variable_to_check} is either a float or an integer.")
else:
    print(f"{variable_to_check} is neither a float nor an integer.")

# 10. Check multiple conditions with comparison and logical operators
height = int(get_user_input("Enter your height (in inches): "))
age = int(get_user_input("Enter your age: "))
adult_permission = get_user_input("Do you have adult permission? (yes/no): ").lower() == "yes"

if (height >= 60 and age >= 16) or adult_permission:
    print("You meet the conditions for this activity.")
else:
    print("You do not meet the conditions for this activity.")
