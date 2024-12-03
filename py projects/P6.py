#start

#   imports

import random

#       score

PS = 0
BS = 0

#       welcome

print("welcome to the rock, paper, scisors.")

#       unlimited trys

while True:

#       player choice

    Pchosse = (str(input("chosse: rock, paper, scisors : ")))
 
#       bot choice
 
    Bchosses = ['rock', 'paper', 'scisors']
    Bchosse = random.choice(Bchosses)

#       chosses

    print("your chosse : " + (str(Pchosse)))
    print("bot chosse : " + (str(Bchosse)))

#       draw

    if Bchosse == Pchosse:
        print("draw")
        print("your score is " + str(PS))
        print("bot score is " + str(BS))

#       bot wons

    elif Bchosse == "rock" and Pchosse == "scisors":
        print("you lose")
        BS = BS+1
        print("your score is " + str(PS))
        print("bot score is " + str(BS))
    elif Bchosse == "paper" and Pchosse == "rock":
        print("you lose")
        BS = BS+1
        print("your score is " + str(PS))
        print("bot score is " + str(BS))
    elif Bchosse == "scisors" and Pchosse == "paper":
        print("you lose")
        BS = BS+1
        print("your score is " + str(PS))
        print("bot score is " + str(BS))

#       player wons

    elif Bchosse == "rock" and Pchosse == "paper":
        print("you won")
        PS = PS+1
        print("your score is " + str(PS))
        print("bot score is " + str(BS))
    elif Bchosse == "paper" and Pchosse == "scisors":
        print("you won")
        PS = PS+1
        print("your score is " + str(PS))
        print("bot score is " + str(BS))
    elif Bchosse == "scisors" and Pchosse == "rock":
        print("you won")
        PS = PS+1
        print("your score is " + str(PS))
        print("bot score is " + str(BS))

#       error

    else:
        print("pls enter valid text")

#end