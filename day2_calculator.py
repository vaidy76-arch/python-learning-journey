print("=== Simple Calculator ===")
print()

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Cannot divide by zero"

# Display results
print()
print(f"Results for {num1} and {num2}:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")

# Bonus: Calculate average
average = (num1 + num2) / 2
print(f"Average: {average}")