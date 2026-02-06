import random

def rps():
    options = ["rock", "paper", "scissors"]
    userinput = str(input("Choose rock, paper, scissors: ")).lower()
    compinput = random.choice(options)
    print("Computer Chose:", compinput)
    if userinput == compinput:
        print("Tie")
    elif userinput == "rock" and compinput == "scissors" or \
        userinput == "paper" and compinput == "rock" or \
        userinput == "scissors" and compinput == "paper":
        print("You win!")
    else: 
        print("Haha you lost, try next time")

rps()
nextgame = True
while nextgame == True:
    anothergame = str(input("Would you like to play another time: "))
    if anothergame.lower() == "yes":
        rps()
    else: 
        nextgame = False
        print("Thanks for playing")
        print("Hope you play again soon")
