# Day 3 Bonus Challenge 4: Rock Paper Scissors

import random

print("=== Rock Paper Scissors ===")
print()

# Computer makes random choice
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)

# Get user choice
user = input("Enter your choice (rock/paper/scissors): ").lower()

if user in ["rock","paper","scissors"]:
# Show choices
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    print()

    if user == computer:
        print("Its a TIE!!")
    else:
        if user=="rock" and computer == "scissors":
            print("You win! 🪨 Rock crushes ✂️ Scissors")
        elif user=="scissors" and computer =="paper":
            print("You win! ✂️ Scissors cuts 📄 Paper")
        elif user=="paper" and computer=="rock":
            print ("You win! 📄 Paper covers 🪨 Rock")
        elif computer =="rock" and user =="scissors":
            print("System Win! 🪨 Rock crushes ✂️ Scissors")
        elif computer =="scissors" and user=="paper":
            print("System win! ✂️ Scissors cuts 📄 Paper")
        elif computer=="paper" and user=="rock":
            print ("Sytem win! 📄 Paper covers 🪨 Rock")
else:
    print("Invalid Entry!! Not in Choice")