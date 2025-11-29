print("=== Simple Calculator Enhanced ===")
print()

# Get user input
operation = input("""Enter Arithmetic Operation you want to perform
                  1. add
                  2. subtract
                  3. mult
                  4. div
                  """)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == "add":
    addition = num1 + num2
    print()
    print(f"Addition result: {addition}")
elif operation == "sub":
    subtraction = num1 - num2
    print()
    print(f"Subtraction result {subtraction}")
elif operation == "mul" :
    multiplication = num1 * num2
    print()
    print(f"Multiplication result: {multiplication}")
elif operation == "div" :
    division = num1/num2 if num2 !=0 else "Divide by 0 not possible"
    print()
    print(f"Division result: {division}")
else:
    print()
    print("None of the available options chosen")



