import random
game=['rock','paper','scissors']
while True:
    computer = random.choice(game)
    human=input("choose one in the following (rock,paper,scissors) : ")
    while human not in game:
        human=input("choose one in the following (rock,paper,scissors) : ")
    print(computer)
    if computer==human:
        print("Tie!")
    elif human == "rock":
        if computer=="scissor":
            print("you won!")
        elif computer=="paper":
            print("computer won!")  
    elif human == "paper":
        if computer=="scissor":
            print("computer won!")
        elif computer=="rock":
            print("you won!")
    elif human == "scissors":
        if computer=="paper":
            print("you won!")
        elif computer=="rock":
            print("computer won!")
    user= input("If you want to play (Yes/No) : ").lower()
    if user!="yes":
        break
print("Bye!")
