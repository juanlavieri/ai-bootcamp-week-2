# Input Order

# Create a variable that takes in the name of an item the user wants to purchase.
item_name = input("What item do you want to purchase? ")

# Use the item variable to ask the user how much the item costs and how many they want:
item_cost_str = input("How much does the item cost? ")
item_quantity_str = input("How many do you want to purchase? ")

# Convert the item cost and quantity to numbers. 
# Consider which type of number type is best for each variable: float or integer?

# Convert item_cost_str to a float (since cost can have decimal values).
item_cost = float(item_cost_str)

# Convert item_quantity_str to an integer (since quantity is typically a whole number).
item_quantity = int(item_quantity_str)

# Print out the values of each of these two new variables, along with their data types, to confirm they were correctly converted.
print("Item Cost:", item_cost, "Data Type:", type(item_cost))
print("Item Quantity:", item_quantity, "Data Type:", type(item_quantity))

# Display a sentence that includes all three variables.
print(f"You want to purchase {item_quantity} {item_name}(s) at a cost of ${item_cost} each.")
