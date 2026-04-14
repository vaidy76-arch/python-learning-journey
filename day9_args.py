# *args collects ALL extra positional arguments into a TUPLE
def add_all(*numbers):
    """
    Add any number of values together.
    
    *numbers collects arguments into a tuple called 'numbers'
    Example: add_all(1, 2, 3) → numbers = (1, 2, 3)
    """
    print(f"Received: {numbers}")  # Shows it's a tuple
    print(f"Type: {type(numbers)}")  # <class 'tuple'>
    
    return sum(numbers)  # sum() works on tuples

# Test it
print(add_all(5, 3))              # (5, 3) → 8
print(add_all(5, 3, 2))           # (5, 3, 2) → 10
print(add_all(1, 2, 3, 4, 5))     # (1, 2, 3, 4, 5) → 15


# CORRECT: Required parameter first, then *args
def multiply_and_add(multiplier, *numbers):
    """
    Multiply each number, then add them.
    
    multiplier: required parameter (must be provided)
    *numbers: optional additional numbers
    """
    print(f"Multiplier: {multiplier}")
    print(f"Numbers to multiply: {numbers}")
    
    # Multiply each number by multiplier, then sum
    total = sum(num * multiplier for num in numbers)
    return total

# Usage
result = multiply_and_add(2, 5, 3, 1)
# multiplier = 2
# numbers = (5, 3, 1)
# Calculation: (5*2) + (3*2) + (1*2) = 10 + 6 + 2 = 18
print(f"Result: {result}")

# WRONG - This would cause an error:
# def bad_function(*numbers, multiplier):  # ERROR!
#     pass


# **kwargs collects ALL extra KEYWORD arguments into a DICTIONARY
def print_info(**details):
    """
    Print information about a person.
    
    **details collects keyword arguments into a dict called 'details'
    Example: print_info(name="Alice", age=25) → details = {'name': 'Alice', 'age': 25}
    """
    print(f"Received: {details}")  # Shows it's a dictionary
    print(f"Type: {type(details)}")  # <class 'dict'>
    
    print("\n--- Person Info ---")
    for key, value in details.items():
        # Capitalize first letter of key for display
        print(f"{key.capitalize()}: {value}")

# Test it
print_info(name="Alice", age=25, city="NYC")
# details = {'name': 'Alice', 'age': 25, 'city': 'NYC'}

print("\n")

print_info(name="Bob", job="Developer", country="USA", hobby="Coding")
# details = {'name': 'Bob', 'job': 'Developer', 'country': 'USA', 'hobby': 'Coding'}

def flexible_function(required, *args, default="default_value", **kwargs):
    """
    Demonstrates all parameter types together.
    
    Order MUST be:
    1. Required positional parameters
    2. *args (optional positional)
    3. Named parameters with defaults
    4. **kwargs (optional keyword)
    """
    print(f"Required parameter: {required}")
    print(f"Extra positional args: {args}")
    print(f"Named parameter: {default}")
    print(f"Extra keyword args: {kwargs}")

# Example call
flexible_function(
    "REQUIRED",           # Goes to 'required'
    "extra1", "extra2",   # Goes to *args → ("extra1", "extra2")
    default="custom",     # Goes to 'default' parameter
    name="Alice",         # Goes to **kwargs → {"name": "Alice", "age": 25}
    age=25
)