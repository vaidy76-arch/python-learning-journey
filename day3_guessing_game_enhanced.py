# Day 3 Practice: Number Guessing Game Enhanced

import random

name= input("Your Name: ")
print(f"Welcome {name}!! Lets play number guessing Game")
print("I'm thinking of a number between 1 and 10")
print()

# Computer picks random number
secret_number = random.randint(1, 10)

# Get user's guess
guess = int(input("Take a guess: "))
difference = abs(guess-secret_number)
if guess == secret_number:
    print(f"You Guessed it right!!")
elif difference <= 2:
    print(f"So Close")
elif difference <=5:
    print(f"You're Warm")
else :
    print(f"You're cold")

print(f"Number I guessed: {secret_number}")


