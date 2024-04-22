""" 
This project demonstrates number guessing game
"""

import random

def main():
    """
    Function implements the game
    """
    random_number = random.randint(1, 100)
    guess = 0
    guesses = set()
    chances = 7

    while guess != random_number and chances != 0:
        print("You have", chances, "chances to guess the number.")
        guess = int(input('Enter a number between 1 and 100:'))

        if guess > 100:
            print("Invalid! Your guess shouldn't be greater than 100.")

        elif guess in guesses:
            print("Number already guessed!!")

        elif guess < random_number:
            print("Your guess is low.")
            chances = chances - 1
            guesses.add(guess)

        elif guess > random_number:
            print("Your guess is high.")
            chances = chances - 1
            guesses.add(guess)

        elif guess == random_number:
            print("Congratulations! You guessed the correct number. The number was", random_number)

    if guess != random_number:
        print("Unfortunately! You lost. The number was", random_number)

if __name__ == "__main__":
    main()
