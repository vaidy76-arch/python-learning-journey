# Day 6: Functions & Modules

print("=== Function Basics ===")
print()

# Defining a simple function
def greet():
    print("Hello!")
    print("Welcome to Python functions!")

# Calling the function
greet()
print()

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")
    print(f"Nice to meet you, {name}!")

greet_person("Alice")
greet_person("Bob")
print()

# Function with multiple parameters
def introduce(name, age, city):
    print(f"Hi! I'm {name}")
    print(f"I'm {age} years old")
    print(f"I live in {city}")

introduce("Alice", 25, "NYC")
print()

# Function with return value
def add(a, b):
    result = a + b
    return result

sum1 = add(5, 3)
print(f"5 + 3 = {sum1}")

sum2 = add(10, 20)
print(f"10 + 20 = {sum2}")

print("\n=== Return Values ===")
print()

# Function that returns a value
def square(number):
    return number ** 2

result = square(5)
print(f"Square of 5: {result}")

# You can use return value directly
print(f"Square of 7: {square(7)}")
print()

# Function that returns multiple values (as tuple)
def get_user_info():
    name = "Alice"
    age = 25
    city = "NYC"
    return name, age, city  # Returns a tuple

# Unpack the returned values
user_name, user_age, user_city = get_user_info()
print(f"Name: {user_name}")
print(f"Age: {user_age}")
print(f"City: {user_city}")
print()

# Function with calculations
def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum

nums = [10, 20, 30, 40, 50]
total, avg, max_val, min_val = calculate_stats(nums)

print(f"Numbers: {nums}")
print(f"Total: {total}")
print(f"Average: {avg}")
print(f"Max: {max_val}")
print(f"Min: {min_val}")


# Default Parameters

print("\n=== Default Parameters ===")
print()

# Function with default parameter
def greet_with_title(name, title=""):
    print(f"Hello, {title} {name}!")

greet_with_title("Alice")              # Uses default "Friend"
greet_with_title("Bob", "Mr.")         # Uses "Mr."
greet_with_title("Charlie", "Dr.")     # Uses "Dr."
print()

# Multiple defaults
def create_profile(name, age=18, country="USA", active=True):
    print(f"Profile: {name}, Age: {age}, Country: {country}, Active: {active}")

create_profile("Alice")                           # All defaults
create_profile("Bob", 25)                         # Custom age
create_profile("Charlie", 30, "UK")               # Custom age and country
create_profile("David", 22, "Canada", False)      # All custom
print()

# Named arguments (keyword arguments)
create_profile(name="Eve", country="France", age=28)  # Any order!
create_profile(age=35, name="Frank")                  # Skip some defaults

# Variable Scope

print("\n=== Variable Scope ===")
print()

# Global variable
global_var = "I'm global!"

def test_scope():
    # Local variable
    local_var = "I'm local!"
    print(f"Inside function: {local_var}")
    print(f"Inside function: {global_var}")  # Can read global

test_scope()
print(f"Outside function: {global_var}")
# print(local_var)  # This would ERROR - local_var doesn't exist outside!

print()

# Modifying variables
count = 0

def increment_wrong():
    # This creates a NEW local variable!
    count = count + 1  # ERROR - tries to use count before defining it
    print(count)

def increment_right():
    global count  # Tell Python to use the global variable
    count = count + 1
    print(f"Count inside: {count}")

print(f"Count before: {count}")
increment_right()
print(f"Count after: {count}")
increment_right()
print(f"Count after again: {count}")

# *args and **kwargs - Variable number of arguments

print("\n=== *args (Variable Arguments) ===")
print()

# *args - accepts any number of positional arguments
def add_all(*numbers):
    total = sum(numbers)
    print(f"Adding: {numbers}")
    return total

print(f"Result: {add_all(1, 2, 3)}")
print(f"Result: {add_all(10, 20, 30, 40, 50)}")
print(f"Result: {add_all(5)}")
print()

# **kwargs - accepts any number of keyword arguments
def print_info(**info):
    print("Information received:")
    for key, value in info.items():
        print(f"  {key}: {value}")

print_info(name="Alice", age=25, city="NYC")
print()
print_info(product="Laptop", price=999, brand="Dell", year=2024)
print()

# Combining regular, *args, and **kwargs
def full_function(required, optional="default", *args, **kwargs):
    print(f"Required: {required}")
    print(f"Optional: {optional}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

full_function("must have", "custom", 1, 2, 3, name="Alice", age=25)


# Docstrings - Documenting your functions

print("\n=== Docstrings ===")
print()

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    """
    return length * width

# Access the docstring
print(calculate_area.__doc__)
print()
print("=========Using Help()=========")
help(calculate_area)
area = calculate_area(5, 3)
print(f"Area: {area}")