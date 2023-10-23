import random

class User:
    ME=input("Plese choose one among the following: Rock, Paper, Scissor\n")
    COMP=random.choice(["Rock","Paper","Scissor"])
    print("You chose",ME,"Computer chose",COMP)
    #print(deci)
    if COMP==ME:
        print("TIE, try again")

    elif ME=="Paper":
            if COMP=="Rock":
                 print("You win, Computer loses")
            else:
                 print("You lose, Computer wins")
    elif ME=="Rock":
            if COMP=="Scissor":
                 print("You win, Computer loses")
            else:
                 print("You lose, Computer wins")

    elif ME=="Scissor":
            if COMP=="Paper":
                 print("You win, Computer loses")
            else:
                 print("You lose, Computer wins")

User()