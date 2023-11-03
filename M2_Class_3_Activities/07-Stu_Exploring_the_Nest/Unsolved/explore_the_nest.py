# List of lists of birds
birds_list = [
    ["Magpie", "Cockatoo", "Hummingbird", "Ostrich", "Bald Eagle", 
     "Emperor Penguin", "Lyrebird", "Peacock", "Toucan", "Helmeted Hornbill"],
    [60, 70, 10, 270, 100, 129, 90, 105, 60, 120],
    [3.5, 45, 5, 40, 30, 20, 30, 15, 20, 30]
]

# List of bird dictionaries
birds_dictionaries = [
    {
        "name": "Magpie",
        "size (cm)": 60,
        "weight (g)": 210,
        "lifespan": 3.5
    },
    {
        "name": "Cockatoo",
        "size (cm)": 70,
        "weight (g)": 900,
        "lifespan": 45
    },
    {
        "name": "Hummingbird",
        "size (cm)": 10,
        "weight (g)": 5,
        "lifespan": 5
    },
    {
        "name": "Ostrich",
        "size (cm)": 270,
        "weight (g)": 136000,
        "lifespan": 40
    },
    {
        "name": "Bald Eagle",
        "size (cm)": 100,
        "weight (g)": 26000,
        "lifespan": 30
    },
    {
        "name": "Emperor Penguin",
        "size (cm)": 129,
        "weight (g)": 112000,
        "lifespan": 20
    },
    {
        "name": "Lyrebird",
        "size (cm)": 90,
        "weight (g)": 5200,
        "lifespan": 30
    },
    {
        "name": "Peacock",
        "size (cm)": 105,
        "weight (g)": 28600,
        "lifespan": 15
    },
    {
        "name": "Toucan",
        "size (cm)": 60,
        "weight (g)": 4180,
        "lifespan": 20
    },
    {
        "name": "Helmeted Hornbill",
        "size (cm)": 120,
        "weight (g)": 2900,
        "lifespan": 30
    }
]

# Print out the data about the 4th bird in birds_list
fourth_bird = birds_list[0][3]
print("Data about the 4th bird in birds_list:")
print("Name:", fourth_bird)
print("Size (cm):", birds_list[1][3])
print("Lifespan:", birds_list[2][3])

# Calculate the total weight (kg) of all the birds in the birds list
total_weight_kg = sum(bird["weight (g)"] for bird in birds_dictionaries) / 1000
print("\nTotal weight of all birds (kg): {:.3f}".format(total_weight_kg))

# Loop through the birds_dictionaries list
size_to_weight_ratios = []
for bird in birds_dictionaries:
    name = bird["name"]
    lifespan = bird["lifespan"]
    size_cm = bird["size (cm)"]
    weight_g = bird["weight (g)"]
    size_to_weight_ratio = size_cm / weight_g

    print("\nName:", name)
    print("Lifespan:", lifespan)
    print("Size (cm):", size_cm)
    print("Weight (g):", weight_g)
    print("Size to Weight Ratio:", size_to_weight_ratio)

    size_to_weight_ratios.append((name, size_to_weight_ratio))

# Find the bird with the highest and lowest size to weight ratio
sorted_ratios = sorted(size_to_weight_ratios, key=lambda x: x[1])
highest_ratio_bird = sorted_ratios[-1]
lowest_ratio_bird = sorted_ratios[0]

print("\nHighest size to weight ratio:", highest_ratio_bird[0])
print("Lowest size to weight ratio:", lowest_ratio_bird[0])
 