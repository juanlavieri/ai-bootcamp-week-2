# Get user input for x and y
x_str = input("Enter the value for x: ")
y_str = input("Enter the value for y: ")

# Convert the input to integers (assuming x and y should be integers)
x = int(x_str)
y = int(y_str)

# Addition problem
addition_result = x + y  # Explanation: We added x and y together.

# Subtraction problem
subtraction_result = x - y  # Explanation: We subtracted y from x.

# Multiplication problem
multiplication_result = x * y  # Explanation: We multiplied x by y.

# Division problem
division_result = x / y  # Explanation: We divided x by y.

# Modulus problem
modulus_result = x % y  # Explanation: We found the remainder of x divided by y.

# Floor division problem
floor_division_result = x // y  # Explanation: We performed integer division of x by y.

# Exponent problem
exponent_result = x ** y  # Explanation: We raised x to the power of y.

# Order of operations problem without parenthesis
order_of_operations_result = x + y * x  # Explanation: We followed the order of operations (multiplication before addition).

# Order of operations problem with parenthesis
order_of_operations_parenthesis_result = (x + y) * x  # Explanation: We used parentheses to prioritize addition before multiplication.

# Print the results of each problem along with explanations
print("Addition Result:", addition_result, "Explanation: We added x and y together.")
print("Subtraction Result:", subtraction_result, "Explanation: We subtracted y from x.")
print("Multiplication Result:", multiplication_result, "Explanation: We multiplied x by y.")
print("Division Result:", division_result, "Explanation: We divided x by y.")
print("Modulus Result:", modulus_result, "Explanation: We found the remainder of x divided by y.")
print("Floor Division Result:", floor_division_result, "Explanation: We performed integer division of x by y.")
print("Exponent Result:", exponent_result, "Explanation: We raised x to the power of y.")
print("Order of Operations Result (Without Parenthesis):", order_of_operations_result, "Explanation: We followed the order of operations (multiplication before addition).")
print("Order of Operations Result (With Parenthesis):", order_of_operations_parenthesis_result, "Explanation: We used parentheses to prioritize addition before multiplication.")
