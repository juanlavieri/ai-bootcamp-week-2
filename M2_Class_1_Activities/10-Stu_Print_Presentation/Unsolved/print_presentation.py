# Declare pi
pi = 3.14159265358979323846

# Print a string that uses the new line character
print("This is a string\nwith a new line.")

# Ask the user for a name and store it as a variable
user_name = input("Enter your name: ")

# Use an f-string to print the name in title case, along with something they
# said that uses both single and double quotation marks
user_input = input("Enter something you said: ")
formatted_text = f"{user_name.title()} said: '{user_input}'"
print(formatted_text)

# Ask the user for the number of dashes that should be displayed in the
# presentation and convert it to an integer
num_dashes = int(input("Enter the number of dashes for the presentation: "))

# Ask the user for the radius of a circle and convert it to a float
radius = float(input("Enter the radius of a circle: "))

# Print out the dashes
dashes = "-" * num_dashes
print(dashes)

# Use a multiline f-string to print out the radius, surface area, and volume
# of a sphere to 4 decimal places using the radius from the user input.
surface_area = 4 * pi * radius ** 2
volume = (4/3) * pi * radius ** 3
formatted_result = f"""
Radius: {radius:.4f}
Surface Area: {surface_area:.4f}
Volume: {volume:.4f}
"""
print(formatted_result)
