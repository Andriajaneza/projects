#start

#   ready?

print("are you ready for play quiz game? Yes or No")
start = (str(input("")))

#   the game

def yes():
    print("question N1")
    print("გრძელო best? Yes or No")
    N1 = (str(input("")))
    if N1 == "Yes":
        print("cool! next!")
        print("question N2")
        print("ფეხბურთი სპორტია? Yes or No")
        N2 = (str(input("")))
        if N2 == "Yes":
            print("cool! next!")
            print("question N2")
        print("გოა ცუდია! Yes or No")
        N3 = (str(input("")))
        if N3 == "yes":
            print("არასწორია")
        if N3 == "no":
                print("!!super!!")
        if N2 == "no":
            print("არასწორია")
    if N1 == "No":
        print("არასწორია!")

#   if not ready

def no():
    print("OK")

#   ready get

if start == "yes":
    yes()
if start == "no":
    no()

#the end