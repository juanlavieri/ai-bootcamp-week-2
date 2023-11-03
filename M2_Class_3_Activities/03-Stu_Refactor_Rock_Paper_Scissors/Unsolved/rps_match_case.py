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

    # Check if the user selected a valid choice
    if user_choice in options:
        # Generate the computer selection
        computer_choice = random.choice(options)
        print("Entered if else")
        # Create variables for user and computer choices using match-case
        match user_choice:
            case "r":
                user_full_choice = "rock"
            case "p":
                user_full_choice = "paper"
            case "s":
                user_full_choice = "scissors"
        
        match computer_choice:
            case "r":
                computer_full_choice = "rock"
            case "p":
                computer_full_choice = "paper"
            case "s":
                computer_full_choice = "scissors"

        # Check the result using match-case statements
        match (user_choice, computer_choice):
            case ("r", "r"), ("p", "p"), ("s", "s"):
                print(f"You both chose {user_full_choice}!")
                print("A smashing tie!")

            case ("r", "s"), ("p", "r"), ("s", "p"):
                print(f"You chose {user_full_choice}")
                print(f"The computer chose {computer_full_choice}.")
                print("Yay! You won.")

            case ("s", "r"), ("r", "p"), ("p", "s"):
                print(f"You chose {user_full_choice}")
                print(f"The computer chose {computer_full_choice}.")
                print("Sorry. You lose.")
    else:
        print("I don't understand that!")
        print("Next time, choose from 'r', 'p', or 's'.")

    # Ask the user if they would like to play again and save the answer as 
    # a variable
    print("Would you like to play again?")
    play_again = input("Type (y) to continue or anything else to exit. ")

    # If the user's answer is not "y" or "Y", break from the loop
    if play_again.lower() != "y":
        break

print("Thank you for playing Rock Paper Scissors. See you next time!")
