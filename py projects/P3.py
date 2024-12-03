import random

print("Welcome to the Number Guessing Game!")
print("I will think of a number between 1 and 100.")
print("Your goal is to guess it correctly.")

def get_guess():
    while True:
        guess = int(input("Enter your guess: "))
        if 1 <= guess <= 100:
            return guess
        else:
            print("Please enter a number between 1 and 100.")

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    
    while not guessed_correctly:
        guess = get_guess()
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")

get_guess()
play_game()