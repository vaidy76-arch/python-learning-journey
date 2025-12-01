# Day 3 Practice: Number Guessing Game

import random

print("=== Number Guessing Game ===")
print("I'm thinking of a number between 1 and 10")
print()

# Computer picks random number
secret_number = random.randint(1, 10)

# Get user's guess
guess = int(input("Take a guess: "))

if guess == secret_number:
    print(f"You Guessed it right!!")
elif guess > secret_number:
    print(f"Too high!!")
else :
    print(f"Too Low!!")

