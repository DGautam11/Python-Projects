import random
options = ["nuke","foot","cockroach"]
user_wins = 0
ties = 0
rounds = 0
while True:
    user_picks = input("Foot,Nuke or Cockroach (Quit ends): ").lower()
    if user_picks == "quit":
        break
    print("You chose: "+user_picks.capitalize())
    randomnum = random.randint(0,2)
    #0:nuke,1:foot,2:cockroach
    computer_picks = options[randomnum]
    print("Computer chose: "+computer_picks.capitalize())
    if computer_picks == user_picks == "nuke":
        print("Both LOSE!")
    elif computer_picks == user_picks :
        print ("It is a tie!")
        ties += 1
    elif user_picks == "foot" and computer_picks == "cockroach":
        print("You WIN!")
        user_wins += 1
    elif user_picks == "nuke" and computer_picks == "foot":
        print("You WIN!")
        user_wins += 1
    elif user_picks == "cockroach" and computer_picks == "nuke":
        print("You WIN!")
        user_wins += 1
    else:
        print("You LOOSE!")
    rounds += 1
print("You played " +str(rounds)+" rounds, and won "+str(user_wins)+" rounds, playing tie in "+str(ties)+" rounds.")
   