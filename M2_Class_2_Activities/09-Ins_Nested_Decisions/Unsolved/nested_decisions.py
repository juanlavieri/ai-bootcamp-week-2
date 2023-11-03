# Nested if-else statements

issue_currency = "EUR"
price = 30.0

# Check if price is not negative (greater than or equal to 0)
if price >= 0:
    # If price is not negative and currency is 'USD' (Dollar).
    if issue_currency == "USD":
        print("Price is in USD.")
    # If price is not negative and currency is 'EUR' (Euro).
    elif issue_currency == "EUR":
        print("Price is in Euro.")
    # If anything other than the above.
    else:
        print("Price is in another currency.")
else:
    # Price is negative.
    print("Price is negative.")

# Nested loops

# Keep looping until we exit the loop
while True:
    # Declare user_number
    user_number = None

    # Keep looping while user_number is not an integer
    while not isinstance(user_number, int):
        # Ask the user how many numbers to loop through
        user_input = input("How many numbers to loop through? ")

        # Validate the input is a number
        if user_input.isdigit():
            user_number = int(user_input)

    # Loop through the numbers (limit the range to 20)
    for i in range(user_number):
        # Print each number in the range
        print(i)

    # Once complete, ask the user if they want to quit
    user_choice = input("Do you want to quit? (yes/no): ")
    if user_choice.lower() == "yes":
        break
