import assets
from assets import user_options, selections
import random

print("Welcome to Steve's Rock paper Scissors CLI Game!")
print("Please choose one of the following numbers [1 - 3] to make your selection.")
print()
print("0 : Rock 🪨")
print("1 : Paper 📃")
print("2 : Scissors ✂️")

user_selection = input("Your choice: ")
computer_selection = random.choice(selections)
print(f"You chose : {user_selection} .")
print(f"The computer chose \n{computer_selection} ")
print(user_selection, computer_selection)

if user_selection == computer_selection:
    print("It's a tie!")
elif user_selection == "0" and computer_selection == "2":
    print("You Lose! Paper beats rock")
elif user_selection == "0" and computer_selection == "3":
    print("You Win! Rock beats scissors")
elif user_selection == "2" and computer_selection == "0":
    print("You Win! Paper beats Rock")
elif user_selection == "2" and computer_selection == "3":
    print("You Lose! Scissors beats Paper ")
elif user_selection == "3" and computer_selection == "0":
    print("You Lose! Rock beats paper. ")
elif user_selection == "3" and computer_selection == "2":
    print("You Win! Scissors beats Paper")







