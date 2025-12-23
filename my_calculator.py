"""
My Calculator Module

A simple calculator with basic operations.
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b (handle division by zero!)"""
    if b == 0:
        return "Can't divide by 0"
    return a / b

def power(base, exponent=2):
    """Raise base to the power of exponent (default is 2)"""
    return base ** exponent

def calculate_average(*numbers):
    """Calculate average of any number of values"""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# Module-level variable
PI = 3.14159

# This code only runs when file is executed directly
# NOT when imported as a module

if __name__ == "__main__":
    print("=" * 50)
    print("Calculator Module - Direct Execution")
    print("=" * 50)
    print()
    
    print("Testing all functions:")
    print(f"Add: 5 + 3 = {add(5, 3)}")
    print(f"Subtract: 10 - 4 = {subtract(10, 4)}")
    print(f"Multiply: 6 * 7 = {multiply(6, 7)}")
    print(f"Divide: 20 / 4 = {divide(20, 4)}")
    print(f"Power: 2^8 = {power(2, 8)}")
    print(f"Average: {calculate_average(10, 20, 30)}")