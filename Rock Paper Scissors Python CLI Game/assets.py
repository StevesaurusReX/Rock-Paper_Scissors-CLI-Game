import random
from random import randint
from secrets import choice

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
symbols = [rock , paper, scissors]


# if computer_selection == 'rock':
#     computer_choice = 0
# elif computer_selection == 'paper':
#     computer_choice = 1
# elif computer_selection == 'scissors':
#     computer_choice = 2


print("Welcome to the rock paper scissors python CLI game! ")
computer_selection = randint(0, 2)


print('\n\nPlease choose one of the following options by typing in its corresponding number :'
      '\n0 : Rock'
      '\n1 : Paper'
      '\n2: Scissors'
      '')

user_selection = int(input('Your selection : '))
print(f"The computer chose : {computer_selection}")
if user_selection == computer_selection:
    print("it's a tie!")
    # Logic conditionals for Rock
elif user_selection == 0 and computer_selection == 1:
    print("You Lose! Rock gets beaten by Paper. ")
elif user_selection == 0 and computer_selection == 2:
    print("You Win! Rock beats Scissors. ")
    # Logic conditionals for Paper
elif user_selection == 1 and computer_selection == 0:
    print("You Win! Paper beats Rock. ")
elif user_selection == 1 and computer_selection == 2:
    print("You Lose! Paper gets beaten by Scissors. ")
    # Logic conditionals for Scissors
elif user_selection == 2 and computer_selection == 0:
    print("You Lose! Scissors gets beaten by Rock. ")
elif user_selection == 2 and computer_selection == 1:
    print("You Win! Scissors beats Paper. ")
else:
    print("invalid input")

# elif user_selection == 0 and computer_selection == 2:
#     print("You Lose! Paper beats rock")
# elif user_selection == 0 and computer_selection == 3:
#     print("You Win! Rock beats scissors")
# elif user_selection == 1 and computer_selection == 0:
#     print("You Win! Paper beats Rock")
# elif user_selection == 1 and computer_selection == 3:
#     print("You Lose! Scissors beats Paper ")
# elif user_selection == 2 and computer_selection == 0:
#     print("You Lose! Rock beats paper. ")
# elif user_selection == 2 and computer_selection == 2:
#     print("You Win! Scissors beats Paper")


