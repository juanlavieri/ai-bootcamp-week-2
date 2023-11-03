# Loop through a range of numbers (0 through 4)
for i in range(5):
    print(i)

print("-" * 40)

# Loop through a range of numbers (2 through 6 - up to, but not including, 7)
for j in range(2, 7):
    print(j)

print("-" * 40)

# Loop through a range of numbers (0 through 4) without using the value in the range
y = 0
for _ in range(5):
    y += 1
    if y == 5:
        continue
    else:
        print(y)


print("-" * 40)

# Iterate through letters in a string
word = "Hello"
for letter in word:
    print(letter)

print("-" * 40)

# Iterate through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("-" * 40)

# Make changes to each item in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)
print(squared_numbers)

print("-" * 40)

# Loop while a condition is being met
run = "y"
while run.lower() == "y":
    print("The loop is running.")
    run = input("Do you want to continue? (y/n): ")

# While loop with a Boolean variable
flag = True
while flag:
    print("This loop runs as long as 'flag' is True.")
    flag = False  # Change 'flag' to False to exit the loop
