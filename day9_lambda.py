# Regular function
def square(x):
    return x ** 2

result = square(5)
print(result)  # 25

# Lambda function (one-liner, anonymous)
square_lambda = lambda x: x ** 2
#result = square_lambda(5)
print(square_lambda(5))  # 25


# Example 1: Add two numbers
add = lambda a, b: a + b
print(add(3, 5))  # 8

# Example 2: Check if even
is_even = lambda n: n % 2 == 0
print(is_even(4))   # True
print(is_even(7))   # False

# Example 3: Get first character
first_char = lambda text: text[0]
print(first_char("Hello"))  # H

# Example 4: Multiple parameters
calculate_area = lambda length, width: length * width
print(calculate_area(5, 3))  # 15

# Example 5: No parameters
get_greeting = lambda: "Hello, World!"
print(get_greeting())  # Hello, World!

# Use Case 1: Sorting by custom criteria
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort by grade (highest first)
sorted_students = sorted(students, key=lambda s: s["grade"], reverse=True)

print("Sorted by grade (highest first):")
for student in sorted_students:
    print(f"{student['name']}: {student['grade']}")

    # Sort by name (alphabetically)
sorted_by_name = sorted(students, key=lambda s: s["name"])
print("\nSorted by name:")
for student in sorted_by_name:
    print(f"{student['name']}: {student['grade']}")

# Sort by name length
sorted_by_name_length = sorted(students, key=lambda s: len(s["name"]))
print("\nSorted by name length:")
for student in sorted_by_name_length:
    print(f"{student['name']} ({len(student['name'])} letters): {student['grade']}")


    # Use Case 2: Filtering lists
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter(function, list) keeps items where function returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"\nEven numbers: {evens}")

# Filter numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"Numbers > 5: {greater_than_5}")

# Filter students with grade >= 85
passing_students = list(filter(lambda s: s["grade"] >= 85, students))
print(f"\nPassing students (grade >= 85):")
for student in passing_students:
    print(f"{student['name']}: {student['grade']}")


    # Use Case 3: Transforming lists
# map(function, list) applies function to each item

# Square each number
squares = list(map(lambda x: x ** 2, numbers))
print(f"\nSquares: {squares}")

# Double each number
doubles = list(map(lambda x: x * 2, numbers))
print(f"Doubles: {doubles}")

# Extract just the names from students
names = list(map(lambda s: s["name"], students))
print(f"\nStudent names: {names}")

# Convert grades to letter grades
def get_letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    else:
        return "F"

# Map grades to letters
letter_grades = list(map(lambda s: get_letter_grade(s["grade"]), students))
print(f"Letter grades: {letter_grades}")