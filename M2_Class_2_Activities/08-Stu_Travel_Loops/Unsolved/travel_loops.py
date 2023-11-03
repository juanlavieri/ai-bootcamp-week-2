# Declare lists
cities = ["Rome", "Nairobi", "Phnom Penh", "Santiago", "Toronto", "Rotorua"]
cities_daily_cost = [150, 70, 60, 80, 110, 125]

# Create a loop to ask the user for a city and append it to the cities list
for _ in range(3):
    user_input = input("Enter a city: ").title()
    cities.append(user_input)

# Create a while loop to get daily costs for cities
while len(cities_daily_cost) < len(cities):
    city_index = len(cities_daily_cost)
    user_input = input(f"Enter the daily cost for {cities[city_index]}: ")
    cities_daily_cost.append(int(user_input))

# Add 10 to each item in the cities_daily_cost list
for i in range(len(cities_daily_cost)):
    cities_daily_cost[i] += 10

# Loop through both lists and print city names and daily costs
for i in range(len(cities)):
    city = cities[i]
    cost = cities_daily_cost[i]
    print(f"Daily cost of {city} is ${cost}")
