# emojy guessing game

print("welcome")

while True:
    A = input("enter emojy : ")
    if A in ['😁','😃','😀','😊','🙂','😚','😎']:
        print("you are happy 😊")
    elif A in ['🤣','😅','😂','😄']:
        print("you are laughing 😂")
    elif A in ['🥰','😍','😘']:
        print("may you love something 😍")
    elif A in ['☹️','🥺','🤧','😰','😧','😖','😞','😓','😔','😕','😟','😩','😭','😢']:
        print("you are sad 🥺")
    elif A in ['🤬','👿','😡']:
        print("you are angry 😡")
    elif A in ['😱','😨']:
        print("you are shocked 😱")
    else:
        print("sorry, i don't know this emojy")
