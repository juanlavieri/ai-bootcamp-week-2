import math  # Import the math module to use the value of pi

# Ask the user what their vacation budget is and convert it to a float
budget = float(input("What is your total vacation budget? "))

# Ask the user how much of their budget should be spent on flights and accommodation and convert it to a float
flights_accommodation = float(input("What is your budget for the flights and accommodation? "))

# Ask the user how much they would like to spend per day and convert it to a float
daily_budget = float(input("What is your preferred daily budget? "))

# Ask the user how many days they will go on vacation and convert it to an integer
vacation_days = int(input("How many days will you go on vacation? "))

# Ask the user the currency exchange rate for the country they're visiting and convert it to a float
exchange_rate = float(input("What is the currency exchange rate? "))

# Ask the user for the radius distance they're willing to walk from their hotel and convert it to a float
distance = float(input("What is the radius distance you're willing to walk from your hotel (in meters)? "))

# Calculate the budget remaining after flights and accommodation
budget_remaining = budget - flights_accommodation

# Calculate the remaining budget in the local currency amount
remaining_budget_local_currency = budget_remaining * exchange_rate

# Calculate the budget per day in the local currency
budget_per_day_local_currency = remaining_budget_local_currency / vacation_days

# Calculate the budget per day in the local currency, ignoring cents
budget_per_day_integer = int(budget_per_day_local_currency)

# Calculate the total area around the hotel the user can walk within
area_of_walk = math.pi * (distance ** 2)

# Calculate the amount left from the budget if the user sticks with their daily budget. This is a modulus problem.
amount_left_with_daily_budget = budget_remaining % (daily_budget * vacation_days)

# Print the results of each calculation
print("Budget Remaining after Flights and Accommodation:", budget_remaining)
print("Remaining Budget in Local Currency:", remaining_budget_local_currency)
print("Budget per Day in Local Currency:", budget_per_day_local_currency)
print("Budget per Day in Local Currency (Ignoring Cents):", budget_per_day_integer)
print("Total Area Around the Hotel for Walking (in square meters):", area_of_walk)
print("Amount Left with Daily Budget:", amount_left_with_daily_budget)
