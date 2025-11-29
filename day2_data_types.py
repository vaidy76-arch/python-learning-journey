# Day 2: Variables and Data Types

# Strings - text data
name = "Alice"
greeting = 'Hello, World!'  # Single or double quotes work
multiline = """This is a
multiline string"""

print(name)
print(type(name))  # <class 'str'>

# Integers - whole numbers
age = 25
year = 2024

print(age)
print(type(age))  # <class 'int'>

# Floats - decimal numbers
height = 5.9
price = 19.99

print(height)
print(type(height))  # <class 'float'>

# Booleans - True or False
is_student = True
has_license = False

print(is_student)
print(type(is_student))  # <class 'bool'>

# Type conversion
age_string = "30"
age_number = int(age_string)  # Convert string to int
print(f"Converted: {age_number}, Type: {type(age_number)}")

price_float = float("25.50")
price_string = str(99.99)

###################################################

# String Operations

first_name = "John"
last_name = "Doe"

# Concatenation
full_name = first_name + " " + last_name
print(full_name)  # John Doe

# String formatting (f-strings - most modern way)
age = 28
message = f"My name is {full_name} and I am {age} years old"
print(message)

# String methods
text = "  hello world  "
print(text.upper())        # HELLO WORLD
print(text.lower())        # hello world
print(text.strip())        # hello world (removes whitespace)
print(text.replace("world", "Python"))  # hello Python

# String indexing and slicing
word = "Python"
print(word[0])      # P (first character)
print(word[-1])     # n (last character)
print(word[0:3])    # Pyt (characters 0 to 2)
print(word[2:])     # thon (from index 2 to end)

# String length
print(len(word))    # 6

# Check if substring exists
sentence = "I love Python programming"
print("Python" in sentence)  # True
print("Java" in sentence)    # False

###############################################################

# Numeric Operations

# Basic arithmetic
a = 11
b = 3

print(f"Addition: {a + b}")           # 13
print(f"Subtraction: {a - b}")        # 7
print(f"Multiplication: {a * b}")     # 30
print(f"Division: {a / b}")           # 3.333...
print(f"Floor Division: {a // b}")    # 3 (rounds down)
print(f"Modulus (remainder): {a % b}") # 1
print(f"Exponentiation: {a ** b}")    # 1000 (10^3)

# Compound operators
count = 5
count += 1  # Same as: count = count + 1
print(f"Count: {count}")  # 6

count *= 2  # Same as: count = count * 2
print(f"Count: {count}")  # 12

# Working with floats
price = 19.99
quantity = 3
total = price * quantity
print(f"Total: ${total:.2f}")  # .2f formats to 2 decimal places

############################################################################