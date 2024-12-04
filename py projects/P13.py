import time
import random

print("welcome to slots!")

l1 = ["🟥","🟧","🟪","🟩","🟦"]

while True:
    start = input("if u want play press enter")
    if start == "":
        time.sleep(0.4)
        print("spining")
        time.sleep(1)
        A = random.choice(l1)
        B = random.choice(l1)
        C = random.choice(l1)
        D = random.choice(l1)
        print(A)
        time.sleep(0.2)
        print(B)
        time.sleep(0.2)
        print(C)
        time.sleep(0.2)
        print(D)
        time.sleep(0.3)
        if A == B and A == C and A == D and A == D:
            print("you won!")
        else:
            print("you lose")
    else:
        print("error")

# ეს არის სლოტები თამაში ამოირჩევს ფერებს თუ ეს ფერები დაემთხვა ერთმანეთს მოიგე თუ არა წააგე