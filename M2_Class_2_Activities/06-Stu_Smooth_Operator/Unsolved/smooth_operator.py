# Gather user input for budget
budget = input("Enter your budget: ")

# Check if budget is a number, and convert it to an integer if it is
if budget.isdigit():
    budget = int(budget)
else:
    print("Error: Please enter a valid budget as a number.")
    exit()

# Declare other variables
cities = ["Rome", "Nairobi", "Phnom Penh", "Santiago", "Toronto", "Rotorua"]
cities_daily_cost = [150, 70, 60, 80, 110, 125]
days = input("How many days can you travel? ")

# Check if `days` is a number, and convert it to an integer if it is
if days.isdigit():
    days = int(days)
else:
    print("Error: Please enter a valid number of days.")
    exit()

# Provide the user with the list of available cities
print("Available cities to visit:")
for i , city in enumerate(cities, start=1):
    print(f"{i}. {city}")

# Ask the user to select a city to visit
city_to_visit = input("Enter the number of the city you would like to visit: ")

# Check if the user input is a valid number within the range of available cities
if city_to_visit.isdigit() and 1 <= int(city_to_visit) <= len(cities):
    city_index = int(city_to_visit) - 1  # Adjust the index for list access
    selected_city = cities[city_index]
    city_daily_cost = cities_daily_cost[city_index]

    # Calculate the total cost of the trip
    total_cost = city_daily_cost * days

    # Check if the traveler can afford the vacation
    if total_cost <= budget:
        remaining_budget = budget - total_cost
        print(f"You can afford your {selected_city} vacation!")
        print(f"Available budget after the trip: ${remaining_budget:.2f}")
    else:
        additional_cost = total_cost - budget
        print(f"You need an additional ${additional_cost:.2f} to afford your {selected_city} vacation.")
else:
    print("Error: Please enter a valid number corresponding to one of the available cities.")
