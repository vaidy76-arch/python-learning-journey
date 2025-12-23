# Day 6: Modules - Importing

print("=== Built-in Modules ===")
print()

# 1. Import entire module
import math

print(f"Pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"2 to the power of 8: {math.pow(2, 8)}")
print()

# 2. Import specific functions
from math import sqrt, pi, ceil, floor

print(f"Pi: {pi}")
print(f"Square root of 25: {sqrt(25)}")
print(f"Ceiling of 4.3: {ceil(4.3)}")    # Rounds up
print(f"Floor of 4.7: {floor(4.7)}")      # Rounds down
print()

# 3. Import with alias (rename)
import random as rnd

print(f"Random number 1-10: {rnd.randint(1, 10)}")
print(f"Random choice: {rnd.choice(['apple', 'banana', 'cherry'])}")
print()

# 4. Import everything (not recommended, but possible)
from datetime import *

now = datetime.now()
print(f"Current date/time: {now}")
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")


# Common Built-in Modules

print("\n=== Common Modules ===")
print()

# os - Operating system operations
import os

print(f"Current directory: {os.getcwd()}")
print(f"Files in directory: {os.listdir('.')[:3]}...")  # First 3 files
print()

# json - Working with JSON (you've used this!)
import json

data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)
print(f"JSON string: {json_string}")

parsed = json.loads(json_string)
print(f"Parsed back: {parsed}")
print()

# time - Time-related functions
import time

print("Waiting 2 seconds...")
start = time.time()
time.sleep(2)  # Pause for 2 seconds
end = time.time()
print(f"Elapsed time: {end - start:.2f} seconds")