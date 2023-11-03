# Function to get user choice
def get_user_choice(prompt):
    while True:
        user_input = input(prompt)
        if user_input in ('1', '2'):
            return user_input
        else:
            print("Invalid input. Please select 1 or 2.")

# Function to check the user's prediction and provide explanations
def check_prediction(code, option1_output, option2_output, correct_option, explanation):
    print(code)
    user_choice = get_user_choice(f"Select 1 for '{option1_output}' or 2 for '{option2_output}': ")
    
    if user_choice == correct_option:
        print("Success! Your choice is correct.")
    else:
        print("Oops! Your choice is incorrect.")
        print(f"Correct Option: {correct_option}")
        print(f"Explanation: {explanation}")

# 1.
code1 = '''
x = 5
if 2 * x > 10:
    print("Question 1 works!")
else:
    print("oooo needs some work")
'''
check_prediction(code1, "Question 1 works!", "oooo needs some work", '2', "The condition 2 * x > 10 evaluates to 2 * 5 > 10, which is False.")

# 2.
code2 = '''
x = 5
if len("Dog") < x:
    print("Question 2 works!")
else:
    print("Still missing out")
'''
check_prediction(code2, "Question 2 works!", "Still missing out", '1', "The length of the string 'Dog' is 3, which is less than x (5).")

# 3.
code3 = '''
x = 2
y = 5
if (x ** 3 >= y):
    print("GOT QUESTION 3!")
else:
    print("This one didn't work")
'''
check_prediction(code3, "GOT QUESTION 3!", "This one didn't work", '1', "The condition x ** 3 >= y evaluates to 2 ** 3 >= 5, which is True.")

# 4.
code4 = '''
country = "Madagascar"
if country == "Madagascar":
    print(f"{country} is in Africa")
else:
    print(f"{country} is not in Africa")
'''
check_prediction(code4, "Madagascar is in Africa", "Madagascar is not in Africa", '1', "The variable 'country' is 'Madagascar', which matches the condition.")

# 5.
code5 = '''
going_places = True
if going_places:
    print("You're going places!")
else:
    print("You prefer to stay at home.")
'''
check_prediction(code5, "You're going places!", "You prefer to stay at home.", '1', "The variable 'going_places' is True, so the if condition is met.")

# 6.
code6 = '''
altitude = "66,000"
if altitude.isdigit():
    print(f"The plane flew at {altitude} feet")
else:
    print(f"{altitude} cannot be converted to a number")
'''
check_prediction(code6, "The plane flew at 66,000 feet", "66,000 cannot be converted to a number", '2', "The variable 'altitude' contains a comma, so it cannot be converted to a number.")
