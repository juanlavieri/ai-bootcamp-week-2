# Prompt the user for their information
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Prompt the user for a list of hobbies (comma-separated)
hobbies_input = input("Enter your hobbies (comma-separated): ")
hobbies = hobbies_input.split(",")

# Prompt the user for wake-up times on different days
wake_up_times = {}
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for day in days:
    time = input(f"Enter your wake-up time for {day}: ")
    wake_up_times[day] = time

# Create a dictionary to store the user's information
your_info = {
    "name": name,
    "age": age,
    "hobbies": hobbies,
    "wake-up": wake_up_times
}

# Print out the user's information
print(f"Your name is {your_info['name']} and you are {your_info['age']} years old.")
print(f"One of your hobbies is {your_info['hobbies'][0]}.")
print(f"You typically wake up at {your_info['wake-up']['Monday']} on Mondays.")

# Use a loop to print out the key-value pairs in the dictionary
print("\nKey-Value Pairs in your_info:")
for key, value in your_info.items():
    print(f"{key}: {value}")

# Use a loop to print out the keys of the wake-up dictionary
print("\nKeys in the 'wake-up' dictionary:")
for day in your_info['wake-up'].keys():
    print(day)

# Use a loop to print out the values of the wake-up dictionary
print("\nValues in the 'wake-up' dictionary:")
for time in your_info['wake-up'].values():
    print(time)
