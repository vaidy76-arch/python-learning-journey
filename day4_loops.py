# Day 4: Loops - For and While

print("=== For Loops ===")
print()

# Basic for loop with range
print("Counting 1 to 5:")
for i in range(1, 6):  # range(start, stop) - stop is NOT included
    print(i)

print()

# Loop with just one number (starts from 0)
print("Counting 0 to 4:")
for i in range(5):  # Same as range(0, 5)
    print(i)

print()

# Loop with step
print("Even numbers 0 to 10:")
for i in range(0, 11, 2):  # range(start, stop, step)
    print(i)

print()

# Looping through a string
print("Letters in 'Python':")
for letter in "Python":
    print(letter)

print()

# Looping through a list
print("Favorite foods:")
foods = ["pizza", "sushi", "tacos", "pasta"]
for food in foods:
    print(f"I love {food}!")

############################################################################

# Useful for loop patterns

# 1. Sum of numbers
print("\n=== Sum of numbers 1 to 10 ===")
total = 0
for num in range(1, 11):
    total += num
    print(f"Current number: {num}, Running total: {total}")
print(f"Final sum: {total}")

# 2. Loop with index using enumerate
print("\n=== Numbered list ===")
fruits = ["apple", "banana", "cherry", "date"]
for index, fruit in enumerate(fruits, 1):  # Start counting from 1
    print(f"{index}. {fruit}")

# 3. Multiplication table
print("\n=== Multiplication table for 5 ===")
for i in range(1, 11):
    result = 5 * i
    print(f"5 x {i} = {result}")

# 4. FizzBuzz pattern (prints numbers but with conditions)
print("\n=== FizzBuzz (1-20) ===")
for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
        

###########################

# While Loops - repeat UNTIL condition becomes False

print("\n=== While Loops ===")


# Basic while loop
print("Countdown:")
count = 5
while count > 0:
    print(count)
    count -= 1  # Decrease count by 1
print("Blast off! 🚀")

print()

# While loop with user input
print("=== Password checker ===")
correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input(f"Enter password (Attempt {attempts + 1}/{max_attempts}): ")
    
    if password == correct_password:
        print("✅ Access granted!")
        break  # Exit the loop immediately
    else:
        attempts += 1
        if attempts < max_attempts:
            print("❌ Wrong password. Try again.")
        else:
            print("❌ Too many attempts. Locked out!")

print()

# Infinite loop with break
print("=== Simple Menu ===")
while True:  # This loops forever until we use 'break'
    print("\n1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        print("Hello! 👋")
    elif choice == "2":
        print("Goodbye! 👋")
    elif choice == "3":
        print("Exiting program...")
        break  # Exit the infinite loop
    else:
        print("Invalid choice. Try again.")

################################################

# Break and Continue statements

print("\n=== Break - stops the loop ===")
for i in range(1, 11):
    if i == 5:
        print("Found 5! Stopping...")
        break  # Exit loop completely
    print(i)

print("\n=== Continue - skips to next iteration ===")
for i in range(1, 11):
    if i % 2 == 0:  # If even number
        continue  # Skip the rest and go to next iteration
    print(i)  # Only odd numbers will be printed

print("\n=== Finding first number divisible by 7 ===")
for num in range(1, 101):
    if num % 7 == 0:
        print(f"First number divisible by 7: {num}")
        break