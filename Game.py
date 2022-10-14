import random

def your():
    yourPick = input("please enter your pick: scissor, paper or rock (or Q/q to quit):")
    return yourPick

def computer():
    computerNum = random.randint(0, 2)
    # computerPick = ""
    if(computerNum == 0):
        # computerPick = "scissor"
        return "scissor"

    elif computerNum == 1:
        # computerPick = "paper"
        return "paper"

    elif computerNum == 2:
        # computerPick = "rock"
        return "rock"

def logic(yourPick, othersPick):
    if(yourPick == "Q" or yourPick == "q"):
        return -2

    if (yourPick == "scissor" and othersPick == "scissor"):
        return 0
    elif (yourPick == "scissor" and othersPick == "paper"):
        return 1
    elif (yourPick == "scissor" and othersPick == "rock"):
        return 0
    elif (yourPick == "paper" and othersPick == "scissor"):
        return 0
    elif (yourPick == "paper" and othersPick == "paper"):
        return 0
    elif (yourPick == "paper" and othersPick == "rock"):
        return 1
    elif (yourPick == "rock" and othersPick == "scissor"):
        return 1
    elif (yourPick == "rock" and othersPick == "paper"):
        return 0
    elif (yourPick == "rock" and othersPick == "rock"):
        return 0

def game():
    yourScore = 0
    computerScore = 0
    rounds = 0
    while(yourScore != 5 and computerScore != 5):
        yourPick = your()
        computerPick = computer()
        print("you choose", yourPick,",",  "while computer chooses", computerPick)

        yourAddScore = logic(yourPick, computerPick)
        if(yourAddScore == -2):
            return "quit"
        yourScore += yourAddScore

        computerScore += logic(computerPick, yourPick)
        
        rounds += 1
    if(yourScore == 5):
        return "you win, and the number of rounds is:" + str(rounds)
    else:
        return "you lose, and the number of rounds is:" + str(rounds)



if __name__ == "__main__":
    flag = True
    while(flag):
        print(game())
        s = input("Do you wanne another round?:(Y / N)")
        if s == "Y" or s == "y":
            flag = True
        elif s == "N" or s == "n":
            flag = False


    