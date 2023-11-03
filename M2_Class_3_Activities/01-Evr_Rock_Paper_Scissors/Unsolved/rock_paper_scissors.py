# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Create a continuous loop so the user can play multiple rounds
while True:
    # User Selection
    user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

    # Check if the user selected a valid choice from the options list
    if user_choice in options:
        # Generate the computer selection
        computer_choice = random.choice(options)

        # Create a variable called user_full_choice to hold the text of the 
        # full word for the user's choice by using a conditional
        if user_choice == "r":
            user_full_choice = "rock"
        elif user_choice == "p":
            user_full_choice = "paper"
        else:
            user_full_choice = "scissors"

        # Run Conditionals to determine the result
        if user_choice == computer_choice:
            # First check if there is a tie
            print(f"You both chose {user_full_choice}!")
            print("A smashing tie!")
        elif (user_choice == "r" and computer_choice == "p") or (user_choice == "p" and computer_choice == "s") or (user_choice == "s" and computer_choice == "r"):
            # Check if the user picked rock and computer picked paper
            # Check if the user picked paper and computer picked scissors
            # Check if the user picked scissors and computer picked rock
            print(f"You chose {user_full_choice}. The computer chose {computer_choice}.")
            print("Sorry. You lose.")
        else:
            # Check if the user picked rock and computer picked scissors
            # Check if the user picked paper and computer picked rock
            # Check if the user picked scissors and computer picked paper
            print(f"You chose {user_full_choice}. The computer chose {computer_choice}.")
            print("Yay! You won.")

        # Ask the user if they would like to play again and save the answer as 
        # a variable
        play_again = input("Do you want to play again? (y/n): ")

        # If the user's answer is not "y" or "Y", break from the loop
        if play_again.lower() != "y":
            break
    else:
        # Print an error if the user didn't select a valid choice
        print("I don't understand that!")
        print("Next time, choose from 'r', 'p', or 's'.")

# Say goodbye if the loop has been exited
print("Thank you for playing Rock Paper Scissors. See you next time!")
