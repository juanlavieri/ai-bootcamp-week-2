# Declare lists
rides = []
prices = []

# Continuous loop to add rides
while True:
    ride_name = input("Enter the name of a ride (type 'q' to quit): ")
    
    # Check if the user wants to quit
    if ride_name.lower() == 'q':
        break
    
    rides.append(ride_name)

    # Continuous loop to get the price of the ride
    while True:
        ride_price_str = input(f"Enter the price of '{ride_name}': ")
        
        # Check if the input is a number
        if ride_price_str.replace(".", "", 1).isdigit():
            ride_price = float(ride_price_str)

            # Check if the price is less than or equal to 15
            if ride_price <= 15:
                prices.append(ride_price)
                break
            else:
                print("Price must be less than or equal to 15. Please try again.")
        else:
            print("Invalid input. Please enter a number for the price.")

# Loop through the rides and prices lists
for i in range(len(rides)):
    ride_name = rides[i]
    ride_price = prices[i]

    # Initialize the discount variable to False
    discount = False

    # Check if the price is greater than $5
    if ride_price > 5:
        # Apply a 10% discount
        ride_price *= 0.90
        discount = True

    # Print ride name and price with 2 decimal places
    print(f"{ride_name} costs ${ride_price:.2f} to ride.")

    # Check if a discount was applied
    if discount:
        print("A discount of 10% is applied.")

    # Print a line of dashes
    print("-" * 40)
