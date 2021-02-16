# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if (computer_choice == "r") and (user_choice == "r"):
    print(f"computer chose Rock and you chose Rock")
    print(f"its a tie!")
elif (computer_choice == "p") and (user_choice == "p"):
    print(f"computer chose Paper and you chose Paper")
    print(f"its a tie!")
elif (computer_choice == "s") and (user_choice == "s"):
    print(f"computer chose Scissors and you chose Scissors")
    print(f"its a tie!")
elif (computer_choice == "r") and (user_choice == "p"):
    print(f"computer chose Rock and you chose Paper")
    print(f"Paper Covers Rock, You Win!")
elif (computer_choice == "r") and (user_choice == "s"):
    print(f"computer chose Rock and you chose Scissors")
    print(f"Rock Smashes Scissors, You Lose..")
elif (computer_choice == "p") and (user_choice == "r"):
    print(f"computer chose Paper and you chose Rock")
    print(f"Paper Covers Rock, You Lose..")
elif (computer_choice == "p") and (user_choice == "s"):
    print(f"computer chose Paper and you chose Scissors")
    print(f"Scissors Cuts Paper, You Win!")
elif (computer_choice == "s") and (user_choice == "r"):
    print(f"computer chose Scissors and you chose Rock")
    print(f"Rock Smashes Scissors, You Win!")
elif (computer_choice == "s") and (user_choice == "p"):
    print(f"computer chose Scissors and you chose Paper")
    print(f"Scissors Cuts Paper, You Lose..")
else :
    print(f"You're doing it wrong, pick r/p/s")
