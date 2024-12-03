#start

#   welcome

print("welcome to the janeza's traslate")

#   forever

while True:
    
#   input

    eng = (input("english word : "))

#   translates

    if eng == "hi" or eng == "hello":
        geo = "გამარჯობა"
        print("georgian word : " + geo)

    if eng == "good morning":
        geo = "დილა მშვიდობია"
        print("georgian word : " + geo)

    if eng == "man":
        geo = "კაცი"
        print("georgian word : " + geo)

    if eng == "girl":
        geo = "გოგო"
        print("georgian word : " + geo)

    if eng == "boy":
        geo = "ბიჭი"
        print("georgian word : " + geo)

    if eng == "chicken":
        geo = "ქათამი"
        print("georgian word : " + geo)
        
    if eng == "animal":
        geo = "ცხოველი"
        print("georgian word : " + geo)

    if eng == "how are you" or eng == "how are you?":
        geo = "რაფრა ხარ?" 
        print("georgian word : " + geo)

    if eng == "thanks":
        geo = "სპასიბა"
        print("georgian word : " + geo)

    if eng == "snake":
        geo = "გველი"
        print("georgian word : " + geo)

    if eng == "georgia":
        geo = "საქართველო"
        print("georgian word : " + geo)

    if eng == "stupid":
        geo = "დებილი"
        print("georgian word : " + geo)

    if eng == "USA" or eng == "america" or eng == "united states of america" or eng == "usa":
        geo = "ამერიკის შეერთებული შტატები"
        print("georgian word : " + geo)

    if eng == "computer" or eng == "pc" or eng == "PC":
        geo = "კომპიუტერი"
        print("georgian word : " + geo)
    
    if eng == "candy":
        geo = "კამფეტი"
        print("georgian word : " + geo)

#   translated words

all_words = [
    'hello','good morning','man',
    'girl','boy','chicken',
    'animal','how are you?','thanks',
    'snake','georgia','stupid',
    'USA','computer','candy'
]

#end