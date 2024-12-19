#random password generator

import random
import time

chars = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '@', '#'
]

password = ""

amount = int(input("how many characters do you want in password? standard 8 : "))

time.sleep(0.4)

print("")
print("generating...")

for i in range(amount):
    char = random.choice(chars)
    password += char

time.sleep(1)

print("")
print("done")

time.sleep(0.3)

print("")
print("your password is " + password)
print("")
