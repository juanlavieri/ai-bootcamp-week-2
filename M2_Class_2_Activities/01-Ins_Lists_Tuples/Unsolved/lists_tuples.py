# Create a list and set it as a list
scores = [92, 87, 68, 75, 96]

# Methods for accessing parts of a list
# Return the value of a list at a given index
value_at_index_2 = scores[2]  # Accesses the element with index 2 (68)

# Return the index of the first object with a matching value
index_of_75 = scores.index(75)  # Returns 3 (index of 75)

# Return a list slice [index_start:index_end]
slice_of_scores = scores[1:4]  # Returns [87, 68, 75] (from index 1 to 3)

# Methods for modifying a list
# Add an element onto the end of a list
scores.append(84)  # Adds 84 to the end of the list

# Change a specified element within a list at the given index
scores[1] = 90  # Changes the second element (87) to 90

# Remove a specified object from a list
scores.remove(68)  # Removes the first occurrence of 68 from the list

# Remove the object at the index specified
removed_value = scores.pop(2)  # Removes and returns the element at index 2 (68)

# Functions for accessing information about a list
# Return the max (or highest value) item in a list
max_score = max(scores)  # Returns 96 (the highest value in the list)

# Return the min (or lowest) item in a list
min_score = min(scores)  # Returns 75 (the lowest value in the list)

# Return the sum of the items in a list
total_score = sum(scores)  # Returns the sum of all scores (e.g., 409)

# Return the length of the list
num_scores = len(scores)  # Returns 4 (the number of elements in the list)

# Use sum and len to calculate average
average_score = sum(scores) / len(scores)  # Calculates the average of the scores

# Create a tuple, a sequence of immutable Python objects that cannot be changed
my_tuple = (1, 2, 3, 'hello')

# Filter out non-integer elements and find the maximum integer value in the tuple
max_tuple_value = max(item for item in my_tuple if isinstance(item, int))

# Print the results
print("Value at index 2:", value_at_index_2)
print("Index of 75:", index_of_75)
print("Slice of scores:", slice_of_scores)
print("Scores after append:", scores)
print("Scores after change:", scores)
print("Removed value:", removed_value)
print("Max score:", max_score)
print("Min score:", min_score)
print("Total score:", total_score)
print("Number of scores:", num_scores)
print("Average score:", average_score)
print("Max tuple value (integer only):", max_tuple_value)
cd 