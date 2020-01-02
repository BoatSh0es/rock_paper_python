from random import randint

options = ["Rock", "Paper", "Scissors"]

ai = options[randint(0, 2)]

human = False

while human == False:
    human = input("Rock, Paper, Scissors?")
    if human == ai:
        print("Tie!")
    elif human == "Rock":
        if ai == "Paper":
            print("You lose!")
        else:
            print("You win!")
    elif human == "Paper":
        if ai == "Scissors":
            print("You lose!")
        else:
            print("You win!")
    elif human == "Scissors":
        if ai == "Rock":
            print("You lose.")
        else:
            print("You win!")
    else:
        print("Invalid")
    human = False
    ai = options[randint(0,2)]