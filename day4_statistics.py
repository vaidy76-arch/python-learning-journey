# Day 4 Bonus: Number Statistics Calculator

print("=== Number Statistics Calculator ===")
print()

numbers = []  # Empty list to store numbers

while True:
    user_input=input(("Enter a number (or 'done' to finish): "))
    if user_input=="done":
        break
    number=float(user_input)
    numbers.append(number)

if len(numbers) == 0:
    print("No numbers entered!")
else:
    # Calculate stats (Python makes this EASY!)
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    minimum = min(numbers)
    maximum = max(numbers)
    
    # Display results
    print("\n=== Statistics ===")
    print(f"Numbers entered: {numbers}")
    print(f"Count: {count}")
    print(f"Sum: {total}")
    print(f"Average: {average}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")