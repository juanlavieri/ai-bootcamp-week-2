# Create our film dictionary
film = {
    "title": "Everything Everywhere All At Once",
    "director": ["Daniel Kwan", "Daniel Scheinert"],
    "cast": [
        "Michelle Yeoh", 
        "Ke Huy Quan", 
        "Jamie Lee Curtis", 
        "Stephanie Hsu", 
        "James Hong",
        "Jenny Slate",
        "Harry Shum Jr.",
        "Tallie Medel"
    ],
    "distributor": "A24",
    "box_office_in_millions": {
        "us": 72.1,
        "uk": 6.2,
        "canada": 5.1,
        "australia": 4.5
    },
    "release_date": {
        "us": "April 8, 2022",
        "uk": "May 13, 2022",
        "canada": "March 25, 2022",
        "australia": "April 14, 2022"
    }
}

# If we don't know all of the keys in the dictionary that we
# may want to access, we can use keys() to list them for us
print("Keys in film dictionary:")
for key in film.keys():
    print(key)

# We may also just want to access a dictionary's values
print("\nValues in film dictionary:")
for value in film.values():
    print(value)

# And we can access each item in the dictionary as a key-value pair 
# as a list of tuples in the format [(key, value)]
print("\nKey-Value Pairs in film dictionary:")
for item in film.items():
    print(item)

# ---------------------------------------------------------------

# Using these dictionary methods, we can iterate through different 
# parts of the dictionary.

# There are two ways to loop through the keys
print("\nLooping through keys:")
for key in film:
    print(key)

print("\nLooping through keys using items():")
for key, value in film.items():
    print(key)

# Looping through a dictionary's values must use the values() method
print("\nLooping through values:")
for value in film.values():
    print(value)

# When looping through each item in a dictionary, we unpack the (key, value)
# tuple so we can use them separately
print("\nLooping through key-value pairs:")
for key, value in film.items():
    print(f"{key}: {value}")
