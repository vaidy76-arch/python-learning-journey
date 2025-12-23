# Using your custom module

print("=== Using My Calculator Module ===")
print()

# Method 1: Import entire module
import my_calculator

result1 = my_calculator.add(10, 5)
print(f"10 + 5 = {result1}")

result2 = my_calculator.multiply(7, 8)
print(f"7 * 8 = {result2}")

print(f"Pi from module: {my_calculator.PI}")
print()

# Method 2: Import specific functions
from my_calculator import subtract, power, calculate_average

result3 = subtract(20, 8)
print(f"20 - 8 = {result3}")

result4 = power(3, 4)
print(f"3^4 = {result4}")

avg = calculate_average(10, 20, 30, 40, 50)
print(f"Average: {avg}")
print()

# Method 3: Import with alias
import my_calculator as calc

print(f"Using alias - 100 / 4 = {calc.divide(100, 4)}")