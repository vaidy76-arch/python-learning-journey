# Day 3: Control Flow and Comparison Operators

# Comparison Operators
a = 10
b = 5

print("=== Comparison Operators ===")
print(f"a = {a}, b = {b}")
print()

# Equal to
print(f"a == b: {a == b}")   # False

# Not equal to
print(f"a != b: {a != b}")   # True

# Greater than
print(f"a > b: {a > b}")     # True

# Less than
print(f"a < b: {a < b}")     # False

# Greater than or equal to
print(f"a >= b: {a >= b}")   # True

# Less than or equal to
print(f"a <= b: {a <= b}")   # False

print()

# Comparisons with strings
name1 = "Alice"
name2 = "alice"
print(f"'{name1}' == '{name2}': {name1 == name2}")  # False (case sensitive!)
print(f"'{name1}'.lower() == '{name2}': {name1.lower() == name2}")  # True

# If/Elif/Else Statements

print("=== Age Checker ===")
age = int(input("Enter your age: "))

if age < 13:
    print("You're a child")
elif age < 18:
    print("You're a teenager")
elif age < 65:
    print("You're an adult")
else:
    print("You're a senior citizen")

print()

# Nested if statements
print("=== Movie Ticket Pricing ===")
age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower()

if age < 12:
    price = 5
    print("Child ticket")
elif age >= 65:
    price = 7
    print("Senior ticket")
else:
    if is_student == "yes":
        price = 8
        print("Student ticket")
    else:
        price = 12
        print("Regular ticket")

print(f"Ticket price: ${price}")

# Logical Operators: and, or, not

print("\n=== Logical Operators ===")

# AND - both conditions must be True
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive!")
else:
    print("You cannot drive")

# OR - at least one condition must be True
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("No work today! 🎉")
else:
    print("Time to work")

# NOT - reverses the boolean
is_raining = False

if not is_raining:
    print("Let's go outside!")
else:
    print("Stay inside")

# Combining multiple conditions
print("\n=== Login System ===")
username = input("Enter username: ")
password = input("Enter password: ")
is_verified = input("Are you verified? (yes/no): ").lower() == "yes"

if (username == "admin" and password == "secret123") or is_verified:
    print("✅ Access granted!")
else:
    print("❌ Access denied!")