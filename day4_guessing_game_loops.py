# Day 4 Practice: Guessing Game with Loops

import random

print("=== Number Guessing Game (5 Attempts) ===")
print("I'm thinking of a number between 1 and 20")
print()

secret_number = random.randint(1, 20)
max_attempts = 5
attempts = 0
remaining_attempt=max_attempts
while attempts<max_attempts:
    guess=int(input("Guess the number:"))
    attempts += 1
    if guess == secret_number:
        print("YAY! You got the guess")
        break
    else:
        if guess>secret_number:
            print("Too High")
        else:
            print("Too Low")
        remaining_attempt=max_attempts-attempts
        print(f"You have {remaining_attempt} attempts Remaining")

if guess == secret_number:  # They won
    print(f"🎉 You WON in {attempts} attempts!")
else:  # They lost (used all attempts)
    print(f"😢 Game Over! The number was {secret_number}")
    print("Better luck next time!")

