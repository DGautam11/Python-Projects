from os import times
import random
from sre_constants import IN
from ssl import Options

user_wins = 0
computer_wins=0
ties = 0

options = ["rock","paper","scissors"]
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit.").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        print("Type rock paper or scissor")
        continue
        
    
    random_number = random.randint(0,2)
    # rock:0, paper:1, scissors:2
    computer_picks = options[random_number]
    print("Computer picked",computer_picks + ".")

    if(user_input == computer_picks):
        print('It is a tie!')
        ties += 1

    elif user_input == "rock" and computer_picks == "scissors":
        print("You won")
        user_wins += 1

    elif user_input == "paper" and computer_picks == "rock":
        print("You won")
        user_wins += 1 
    
    elif user_input == "scissors" and computer_picks == "paper":
        print("You won!")
        user_wins += 1
    
    else:
        print("You lost!")
        print("Computer wins")
        computer_wins += 1

print("You won",user_wins,"times")
print("The computer won",computer_wins,"times")
print('Ties',ties,'times')
print("GoodBye")

