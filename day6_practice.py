# Day 6 Practice: Calculator Functions

def add(a, b):
    """Add two numbers"""
    #add=a+b
    return a+b
    
def subtract(a, b):
    """Subtract b from a"""
    sub=(a-b)
    return sub
    
def multiply(a, b):
    """Multiply two numbers"""
    mul=a*b
    return mul
    
def divide(a, b):
    """Divide a by b (handle division by zero!)"""
    if(b==0):
        divide="Can't divide by 0"
        return divide
    else:
        divide=a/b
        return divide 
    
def power(base, exponent=2):
    """Raise base to the power of exponent (default is 2)"""
    power=base**exponent
    return power
    
def calculate_average(*numbers):
    """Calculate average of any number of values"""
    average=sum(numbers)/len(numbers)
    return average

# Test your functions
print("=== Calculator Functions ===")
print()

print(f"Add: 5 + 3 = {add(5, 3)}")
print(f"Subtract: 10 - 11 = {subtract(10, 11)}")
print(f"Multiply: 6 * 7 = {multiply(6, 7)}")
print(f"Divide: 20 / 7 = {divide(20, 7)}")
print(f"Divide by zero: {divide(10, 0)}")  # Should handle error!
print()

print(f"Power: 5^3 = {power(5, 3)}")
print(f"Square: 5^2 = {power(5)}")  # Uses default exponent=2
print()

print(f"Average of 10, 20, 30: {calculate_average(10, 20, 30)}")
print(f"Average of 5, 10, 15, 20, 25: {calculate_average(5, 10, 15, 20, 25)}")
