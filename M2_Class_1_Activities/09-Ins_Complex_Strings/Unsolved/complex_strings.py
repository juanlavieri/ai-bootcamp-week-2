# Double quotes (") and single quotes (') can be used interchangeably, but the
# same type of quotation mark must be used to open and close the string.
# It is best practice to remain consistent with your use of quotation marks.
# If a string needs to include one type of quotation mark, you can use the
# other kind to open and close the string.

# What if you want to use both types of quotation marks in your string?
# Then you can use the backslash (\) escape character. This tells Python to
# treat the following character differently than it ordinarily would.

# You can also use triple quotes to print over multiple lines.

# Often, we don't want to use triple quotes to store text across multiple
# lines, as the text can't be indented when we get to complex decisions.
# In those situations, we can insert a new line character instead.

# Print a new line character: \n

# Explain what we want to achieve with user input and gather input accordingly

# Concatenate the two strings with a new line in between
input1 = input("Enter the first string: ")
input2 = input("Enter the second string: ")
concatenated_string = input1 + "\n" + input2

# Print the concatenated result and explain how it was created
print("Concatenated String with a New Line:")
print(f"The concatenated string is:\n{concatenated_string}")

# Explain and gather input for formatting options

# f-strings
name = input("Enter your name: ")
age = input("Enter your age: ")

# Explain the f-string and how it inserts user input
print(f"Hello, my name is {name} and I am {age} years old.")

# Repeating strings
repeating_character = input("Enter a character to repeat: ")
repeating_count = int(input("Enter the number of times to repeat it: "))

# Explain the string repetition and how it's based on user input
repeated_string = repeating_character * repeating_count
print(f"Repeated String: {repeated_string}")

# Lowercase strings
text = input("Enter a text to convert to lowercase: ")

# Explain the lowercase conversion
lowercase_text = text.lower()
print(f"Lowercase Text: {lowercase_text}")

# Uppercase strings
text = input("Enter a text to convert to uppercase: ")

# Explain the uppercase conversion
uppercase_text = text.upper()
print(f"Uppercase Text: {uppercase_text}")

# Title case strings
text = input("Enter a text to convert to title case: ")

# Explain the title case conversion
title_case_text = text.title()
print(f"Title Case Text: {title_case_text}")

# Explain the use of multiline text
print("Here's an example of multiline text using the previous inputs:")
formatted_multiline_text = f"""
This is the entered multiline text:
Input 1: {input1}
Input 2: {input2}
Name: {name}
Age: {age}
Repeated String: {repeated_string}
Lowercase Text: {lowercase_text}
Uppercase Text: {uppercase_text}
Title Case Text: {title_case_text}
"""
print(formatted_multiline_text)

# Simplified the float exercise
decimal_places = int(input("Enter the number of decimal places for Pi (e.g., 2): "))
pi = 3.14159265359
formatted_pi = f"{pi:.{decimal_places}f}"
print(f"Formatted Pi with {decimal_places} decimal places: {formatted_pi}")

# Add thousands comma to a number
number = int(input("Enter a number (e.g., 1000000): "))

# Explain the addition of a thousands comma
formatted_number = f"{number:,}"
print(f"Formatted Number: {formatted_number}")

# Create a string of dashes
dash_count = int(input("Enter the number of dashes to create (e.g., 50): "))

# Explain the creation of a string with dashes
dashes = "-" * dash_count
print(f"Dashes: {dashes}")
