from fuzzywuzzy import fuzz, process

# Create a tuple containing the names of menu sections
menu_sections = ("snacks", "meals", "drinks", "dessert")
print("Menu Sections:", menu_sections)

# Pre-generate items and prices for each menu section
menu = {
    "snacks": ["Chips", "Nachos", "Mozzarella Sticks"],
    "meals": ["Burger", "Pizza", "Pasta", "Salad"],
    "drinks": ["Soda", "Water", "Iced Tea"],
    "dessert": ["Cheesecake", "Ice Cream", "Chocolate Cake"],
}

prices = {
    "snacks": [4.99, 5.99, 6.99],
    "meals": [10.99, 12.99, 9.99, 8.99],
    "drinks": [1.99, 1.49, 2.49],
    "dessert": [5.49, 4.99, 6.99],
}

# Function to get a valid menu section input from the user
def get_valid_menu_section_input():
    while True:
        section = input("Enter a menu section (snacks, meals, drinks, dessert): ").lower()
        if section in menu:
            return section
        else:
            # Suggest corrections for potential typos
            suggestions = process.extractOne(section, menu_sections)
            if suggestions[1] >= 85:  # Suggest a correction if the similarity score is 85% or higher
                confirmation = input(f"Did you mean '{suggestions[0]}'? (yes/no): ").lower()
                if confirmation == 'yes':
                    return suggestions[0]
            print("Invalid menu section. Please try again.")

# Function to get a valid menu item input from the user
def get_valid_menu_item_input(section):
    while True:
        item = input(f"Enter a new item for {section} section (or 'cancel' to skip): ")
        if item.lower() == 'cancel':
            return None
        elif item:
            return item
        else:
            print("Item name cannot be empty. Please try again.")

# Function to get a valid price input from the user
def get_valid_price_input(item):
    while True:
        try:
            price = float(input(f"Enter the price for {item}: "))
            if price >= 0:
                return price
            else:
                print("Price must be a non-negative number. Please try again.")
        except ValueError:
            print("Invalid price format. Please enter a valid number.")

# Function to delete an item from a menu section
def delete_menu_item(section):
    while True:
        print(f"Current items in {section.capitalize()} Section:")
        for i, item in enumerate(menu[section]):
            print(f"{i + 1}. {item}")
        
        item_to_remove = input(f"Enter the name of the item to remove from the {section} section (or 'cancel' to exit): ").capitalize()
        
        if item_to_remove.lower() == 'cancel':
            return False
        
        if item_to_remove in menu[section]:
            item_index = menu[section].index(item_to_remove)
            
            # Remove the item from the menu list using `remove()`
            menu[section].remove(item_to_remove)
            
            # Remove the item from the prices list using `pop()`
            removed_price = prices[section].pop(item_index)
            
            print(f"\n'{item_to_remove}' has been removed from the {section} section.")
            print(f"Price of removed item: ${removed_price:.2f}\n")
        else:
            print(f"'{item_to_remove}' is not found in the {section} section.\n")

# Ask the user if they want to add or delete an item
while True:
    choice = input("Would you like to add or delete an item from the menu? (add/delete/exit): ").lower()
    
    if choice == 'add':
        # Get a valid menu section input from the user
        section = get_valid_menu_section_input()
    
        # Get a valid menu item input from the user
        new_item = get_valid_menu_item_input(section)
        if new_item:
            # Add the new item to the selected menu section
            menu[section].append(new_item)

            # Get a valid price input from the user
            new_price = get_valid_price_input(new_item)
            if new_price is not None:
                # Add the new price to the prices list
                prices[section].append(new_price)
                print(f"\n'{new_item}' has been added to the {section} section.")
                print(f"Price of added item: ${new_price:.2f}\n")
    elif choice == 'delete':
        # Get a valid menu section input from the user
        section = get_valid_menu_section_input()
    
        # Delete an item from the selected menu section
        deleted = delete_menu_item(section)
        if not deleted:
            continue
    elif choice == 'exit':
        # If the user exits, ask for a section to calculate the rest of the script
        section = get_valid_menu_section_input()

        # Calculate and print the total cost if someone bought every item in the specific section
        total_cost = sum(prices[section])
        print(f"\nTotal cost if someone bought every item in the {section.capitalize()} Section: ${total_cost:.2f}")

        # Find the most expensive price on the menu for the specific section
        most_expensive_price = max(prices[section])
        print(f"\nMost Expensive Item in the {section.capitalize()} Section:")
        for i, price in enumerate(prices[section]):
            if price == most_expensive_price:
                print(f"{menu[section][i]}: ${price:.2f}")

        # Find the cheapest price on the menu for the specific section
        cheapest_price = min(prices[section])
        print(f"\nCheapest Item in the {section.capitalize()} Section:")
        for i, price in enumerate(prices[section]):
            if price == cheapest_price:
                print(f"{menu[section][i]}: ${price:.2f}")

        # Confirm that the menu and price lists are the same length
        if len(menu[section]) == len(prices[section]):
            print("\nThe menu and price lists have the same length.")
        else:
            print("\nThe menu and price lists have different lengths.")
        break
