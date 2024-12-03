import random
RN = random.randint(0, 10)

def game():
    print("guess number 0 - 10")
    G = int(input(""))
    if G is RN:
        print("you guessed")
    if G > RN:
        print("you not guessed")
    if G < RN:
        print("you not guessed")
    
game()