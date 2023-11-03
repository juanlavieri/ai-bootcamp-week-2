# Unlike lists, dictionaries store information in pairs
# ---------------------------------------------------------------

# Create a dictionary to hold the actor's names.
actors = {}

# Create a dictionary using the built-in function.
movies = dict()

# A dictionary of an actor.
actor_info = {
    "name": "Denzel Washington",
    "age": 67,
    "movies": ["Training Day", "Flight", "Malcolm X"]
}

# Add an actor to the dictionary with the key "name" and the value "Denzel Washington".
actors["actor1"] = "Denzel Washington"

# Print the actors dictionary.
print(actors)

# Print only the actor.
print(actors["actor1"])

# A list of actors
actors_list = ["Tom Hanks", "Brad Pitt", "Meryl Streep"]

# Overwrite the value, "Denzel Washington", with the list of actors.
actors["actor1"] = actors_list

# Print the first actor
print(actors["actor1"][0])



# ---------------------------------------------------------------

# A dictionary can contain multiple pairs of information


# ---------------------------------------------------------------

# A dictionary can contain multiple types of information


# ---------------------------------------------------------------

# A dictionary can even contain another dictionary


# ---------------------------------------------------------------
