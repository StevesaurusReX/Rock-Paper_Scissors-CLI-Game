import assets
import random







print("Welcome to the rock paper scissors python CLI game! ")
computer_selection = random.randint(0, 2)


print('\n\nPlease choose one of the following options by typing in its corresponding number :'
      '\n0 : Rock'
      '\n1 : Paper'
      '\n2: Scissors'
      '')

user_selection = int(input('Your selection : '))
print(f"The computer chose : {computer_selection}")

if user_selection == computer_selection:
    print(assets.tie)
    print("it's a tie!")
    # Logic conditionals for Rock
elif user_selection == 0 and computer_selection == 1:
    print('you chose rock!\n')
    print(assets.rock)
    print('The computer chose Paper!\n')
    print(assets.paper)
    print("\nYou Lose! Rock gets beaten by Paper. \n")

elif user_selection == 0 and computer_selection == 2:
    print('you chose rock!\n')
    print(assets.rock)
    print('The computer chose Scissors!\n')
    print(assets.scissors)
    print("You Win! Rock beats Scissors. ")

    # Logic conditionals for Paper
elif user_selection == 1 and computer_selection == 0:
    print('you chose Paper!\n')
    print(assets.paper)
    print('The computer chose Rock!\n')
    print(assets.rock)
    print("You Win! Paper beats Rock. ")

elif user_selection == 1 and computer_selection == 2:
    print('you chose Paper!\n')
    print(assets.paper)
    print('The computer chose Scissors!\n')
    print(assets.scissors)
    print("You Lose! Paper gets beaten by Scissors. ")

    # Logic conditionals for Scissors
elif user_selection == 2 and computer_selection == 0:
    print('you chose Scissors!\n')
    print(assets.scissors)
    print('The computer chose Rock!\n')
    print(assets.rock)
    print("You Lose! Scissors gets beaten by Rock. ")

elif user_selection == 2 and computer_selection == 1:
    print('you chose Scissors!\n')
    print(assets.scissors)
    print('The computer chose Paper!\n')
    print(assets.paper)
    print("You Win! Scissors beats Paper. ")

else:
    print("invalid input")







