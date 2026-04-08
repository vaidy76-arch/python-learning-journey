# Day 2 Notes

## What I Learned
- Data types: str, int, float, bool
- F-strings are the best way to format strings
- // is different from / for division


# Day 5 Notes

## Key Learnings

### Dictionaries are Flexible!
- Can add new keys anytime: `student["average"] = 84.5`
- Don't need to predefine structure (unlike C structs)
- Can check if key exists: `if "key" in dict:`

### Lambda Functions
- `lambda x: x[1]` - anonymous function for quick operations
- Used with max(), min(), sorted() for custom comparisons

### My Questions
- Q: Why not add average to same dictionary?
- A: You CAN! Just do `student["average"] = avg`


## Exception Hierarchy for Files
```
BaseException
 └── Exception
      └── OSError (base for most file errors)
           ├── FileNotFoundError
           ├── PermissionError
           ├── FileExistsError
           ├── IsADirectoryError
           ├── NotADirectoryError
           └── IOError (alias for OSError in Python 3+)




dir(module) : List all attributes/functions
help(module) : Full documentation
help(module.function): Help on specific function
module.__doc__ : Module docstring
module.function.__doc__ : Function docstring
inspect.getmembers(module) : Detailed inspection


# Python Learning Journey - Notes

## Overview
6-month learning path to become a full-stack developer
Daily commitment: 1 hour/day
Start date: December 2024

---

## Week 1: Python Fundamentals

### Day 1: Environment Setup
**Date Completed:** ✅

**What I Learned:**
- Installed Python 3.11+, VS Code, Git
- Set up virtual environments (venv)
- Created first GitHub repository
- Basic Git workflow (add, commit, push)

**Key Commands:**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
git add .
git commit -m "message"
git push
```

**Notes:**
- Always activate venv before working
- .gitignore to exclude venv from Git

---

### Day 2: Variables & Data Types
**Date Completed:** ✅

**What I Learned:**
- Data types: str, int, float, bool
- Type conversion: int(), float(), str()
- String operations and f-strings
- Arithmetic operators (+, -, *, /, //, %, **)

**Key Concepts:**
```python
# F-strings (modern formatting)
name = "Alice"
age = 25
print(f"My name is {name}, I'm {age}")

# Division operators
10 / 3   # 3.333... (regular division)
10 // 3  # 3 (floor division)
10 % 3   # 1 (modulus/remainder)

# Type conversion
age_string = "25"
age_number = int(age_string)
```

**Projects Built:**
- Simple calculator
- Enhanced calculator with user choice

**Questions/Confusions:**
- None - concepts clear!

---

### Day 3: Control Flow (if/elif/else)
**Date Completed:** ✅

**What I Learned:**
- Comparison operators: ==, !=, <, >, <=, >=
- Logical operators: and, or, not
- If/elif/else structure
- Nested conditions

**Key Concepts:**
```python
# elif is Python's "else if"
if condition1:
    # code
elif condition2:
    # code
else:
    # code

# Logical operators
if age >= 18 and has_license:
    print("Can drive")

if is_weekend or is_holiday:
    print("No work!")
```

**Projects Built:**
- Number guessing game
- Grade calculator
- Login system with admin
- Rock Paper Scissors game

**Important Notes:**
- Use `in ["option1", "option2"]` for checking multiple values
- Python is case-sensitive: "Rock" != "rock"

---

### Day 4: Loops (For & While)
**Date Completed:** ✅

**What I Learned:**
- For loops with range()
- While loops and infinite loops
- Break and continue statements
- Loop with enumerate() for indexing

**Key Concepts:**
```python
# For loop
for i in range(1, 6):  # 1 to 5 (6 not included!)
    print(i)

# While loop
while condition:
    # code
    if done:
        break

# Enumerate for index + value
for index, item in enumerate(items, 1):  # Start at 1
    print(f"{index}. {item}")

# List comprehension (advanced)
squares = [x**2 for x in range(1, 6)]
evens = [x for x in numbers if x % 2 == 0]
```

**Projects Built:**
- Guessing game with multiple attempts
- Pattern printer (4 patterns)
- Shopping cart calculator
- Number statistics calculator

**Important Notes:**
- `range(5)` = 0,1,2,3,4 (starts at 0)
- `range(1, 6)` = 1,2,3,4,5 (stop not included)
- `range(0, 11, 2)` = 0,2,4,6,8,10 (step by 2)

---

### Day 5: Lists & Tuples
**Date Completed:** ✅

**What I Learned:**
- List methods: append, remove, pop, insert, sort, reverse
- List slicing: `list[start:stop:step]`
- List comprehensions
- Tuples (immutable lists)
- Lambda functions
- File I/O with JSON
- Exception handling (try/except)

**Key Concepts:**

**Lists:**
```python
# List methods
fruits = ["apple", "banana"]
fruits.append("cherry")        # Add to end
fruits.insert(1, "orange")     # Insert at index
fruits.remove("banana")        # Remove by value
fruits.pop()                   # Remove last
fruits.pop(0)                  # Remove by index

# List slicing
numbers = [0, 1, 2, 3, 4, 5]
numbers[2:5]    # [2, 3, 4] (stop not included!)
numbers[:3]     # [0, 1, 2] (first 3)
numbers[3:]     # [3, 4, 5] (from index 3)
numbers[-3:]    # [3, 4, 5] (last 3)
numbers[::2]    # [0, 2, 4] (every 2nd)
numbers[::-1]   # [5, 4, 3, 2, 1, 0] (reverse!)

# List comprehension
squares = [x**2 for x in range(1, 6)]
evens = [x for x in numbers if x % 2 == 0]
```

**Tuples:**
```python
# Immutable - can't change after creation
coordinates = (10, 20)
colors = ("red", "green", "blue")

# Tuple unpacking
x, y = coordinates
name, age, city = ("Alice", 25, "NYC")

# When to use:
# Lists: data will change (add/remove)
# Tuples: data should NOT change (coordinates, dates)
```

**File I/O & JSON:**
```python
import json

# Save to file (overwrites!)
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Load from file
with open("data.json", "r") as f:
    data = json.load(f)

# Exception handling
try:
    with open("file.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Invalid JSON")
except Exception as e:
    print(f"Error: {e}")
```

**Projects Built:**
- Student grade manager
- Complete Todo List Manager with:
  - Add, view, edit, delete tasks
  - Mark complete
  - Statistics
  - Save/load from JSON file
  - Full error handling

**Important Notes:**
- Lists vs Tuples: Lists are mutable, Tuples are immutable
- JSON vs JSONL: JSON for single object, JSONL for line-by-line logs
- File modes: "r" (read), "w" (write/overwrite), "a" (append)
- Exception hierarchy: specific exceptions before general ones

**Key Realizations:**
- Python dictionaries are like JSON!
- Lists are like arrays in other languages
- Can dynamically add keys to dictionaries: `dict["new_key"] = value`

---

### Day 6: Functions & Modules
**Date Completed:** ✅

**What I Learned:**
- Defining functions with parameters
- Return values (single and multiple)
- Default parameters
- Variable scope (local vs global)
- *args and **kwargs
- Docstrings
- Importing modules
- Creating custom modules
- `if __name__ == "__main__"` pattern

**Key Concepts:**

**Functions:**
```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

# Multiple returns (returns tuple)
def get_stats(numbers):
    return sum(numbers), max(numbers), min(numbers)

total, maximum, minimum = get_stats([1, 2, 3])

# Default parameters
def greet(name, title="Friend"):
    return f"Hello, {title} {name}!"

greet("Alice")           # Uses default "Friend"
greet("Bob", "Dr.")      # Uses "Dr."

# *args - variable number of arguments
def add_all(*numbers):
    return sum(numbers)

add_all(1, 2, 3)         # Works with any number!

# **kwargs - keyword arguments
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")

# Docstrings
def calculate_area(length, width):
    """
    Calculate area of rectangle.
    
    Parameters:
        length (float): The length
        width (float): The width
    
    Returns:
        float: The area
    """
    return length * width
```

**Scope:**
```python
count = 0  # Global

def increment():
    global count  # Use global variable
    count += 1

# Without 'global', creates new local variable!
```

**Modules:**
```python
# Import entire module
import math
result = math.sqrt(16)

# Import specific items
from math import sqrt, pi
result = sqrt(16)

# Import with alias
import my_calculator as calc
result = calc.add(5, 3)

# Explore module
dir(math)           # List all functions
help(math.sqrt)     # Get documentation
```

**Creating Modules:**
```python
# my_calculator.py
def add(a, b):
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    # This only runs when file is executed directly
    # NOT when imported as module
    print("Testing:", add(5, 3))
```

**Projects Built:**
- Calculator functions module
- Custom utility module
- Reusable, documented code

**Important Notes:**
- Default parameters must come AFTER required parameters
- `if __name__ == "__main__":` is optional but useful for testing
- Python scans entire function before executing (not line-by-line!)
- File modes: "w" overwrites, "a" appends

**Key Realizations:**
- Functions make code reusable
- Modules organize code into files
- `if __name__ == "__main__":` great for troubleshooting!
- Docstrings accessed via `function.__doc__`

---

## Comparison: Python vs C

**Coming from C, Python is easier because:**
- ✅ No manual memory management
- ✅ Dynamic lists (no fixed size)
- ✅ Built-in functions (sum, max, min, etc.)
- ✅ Automatic garbage collection
- ✅ Rich standard library

**Example:**
```c
// C - Finding max (manual loop)
int max = arr[0];
for(int i = 1; i < size; i++) {
    if(arr[i] > max) max = arr[i];
}
```
```python
# Python - Finding max (built-in)
max_num = max(numbers)
```

**But C taught me:**
- How things work under the hood
- Memory management concepts
- Algorithm fundamentals
- Makes me appreciate Python's convenience!

---

## Key Python Concepts

### String Operations
```python
text = "hello"
text.upper()           # "HELLO"
text.lower()           # "hello"
text.strip()           # Remove whitespace
text.replace("h", "H") # "Hello"
text.split()           # Split into list

# Slicing works like lists
text[0]      # "h" (first char)
text[-1]     # "o" (last char)
text[1:4]    # "ell" (index 1-3)
text[::-1]   # "olleh" (reverse)
```

### Data Structures Quick Reference
```python
# List - ordered, mutable
fruits = ["apple", "banana"]

# Tuple - ordered, immutable
coordinates = (10, 20)

# Dictionary - key-value pairs (like JSON!)
person = {"name": "Alice", "age": 25}

# Can add keys dynamically
person["city"] = "NYC"
```

### File Handling
```python
# Text file
with open("file.txt", "r") as f:
    content = f.read()

# JSON file
import json
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
```

---

## Common Patterns I've Learned

### Input Validation
```python
choice = input("Enter choice (1-5): ")

if choice not in ["1", "2", "3", "4", "5"]:
    print("Invalid choice!")
```

### Menu System
```python
while True:
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")
    
    choice = input("Choose: ")
    
    if choice == "3":
        break
```

### Error Handling
```python
try:
    # Risky code
    result = operation()
except SpecificError:
    # Handle specific error
    pass
except Exception as e:
    # Handle any other error
    print(f"Error: {e}")
```

---

## Projects Completed

1. ✅ Simple Calculator
2. ✅ Enhanced Calculator
3. ✅ Number Guessing Game (multiple versions)
4. ✅ Grade Calculator
5. ✅ Login System
6. ✅ Rock Paper Scissors
7. ✅ Pattern Printer
8. ✅ Shopping Cart
9. ✅ Statistics Calculator
10. ✅ Student Grade Manager
11. ✅ **Todo List Manager (with file persistence!)**
12. ✅ Custom Calculator Module

---

## Best Practices I've Learned

✅ Use f-strings for formatting  
✅ Use `in` for checking multiple values  
✅ Default parameters make functions flexible  
✅ List comprehensions for concise code  
✅ Always handle exceptions when doing file I/O  
✅ Use docstrings to document functions  
✅ `if __name__ == "__main__":` for testing  
✅ Specific exceptions before general ones  
✅ Virtual environments for each project  

---

## Questions Answered

**Q: Why does slicing confuse me?**  
A: Because in `numbers[2:5]`, values and indices both start at 0, making it confusing! Using different data (like letters) makes it clearer.

**Q: Does split() use space as delimiter?**  
A: Yes! `split()` with no argument splits on any whitespace. Can specify delimiter: `split(",")`

**Q: Why error when using `count = count + 1` in function?**  
A: Python scans entire function first. Seeing assignment makes `count` local for whole function, so it tries to read local `count` before it exists! Use `global count` to fix.

**Q: Is `if __name__ == "__main__":` mandatory?**  
A: No! But useful for testing and troubleshooting. Code inside only runs when file executed directly, not when imported.

**Q: Can I append to JSON files?**  
A: Not really for valid JSON. Use "w" mode (overwrites). But JSONL (newline-delimited JSON) is perfect for appending logs!

---

## Tools & Resources

**Installed:**
- Python 3.11+
- VS Code with Python extension
- Git

**Useful Commands:**
```bash
python --version
pip list
dir()              # List module contents
help(function)     # Get documentation
```

**File Extensions:**
- `.py` - Python files
- `.json` - JSON data files
- `.jsonl` - Line-delimited JSON (for logs)
- `.md` - Markdown (documentation)

---

## Daily Work Context

I work with CSV and XLSX files daily, so Python will be great for:
- Automating Excel/CSV processing
- Data analysis
- Report generation
- File format conversions

Python libraries for this (to learn later):
- `pandas` - Excel/CSV operations
- `openpyxl` - Excel files
- `csv` - CSV operations

---

## Next Steps

**Week 1 Complete! (Almost)**
- Day 7: Review & Capstone Project

**Week 2 Preview:**
- More advanced data structures
- Object-Oriented Programming
- Working with files and data
- Building larger applications

---

## Reflections

**What's going well:**
- Consistent daily practice (6 days straight!)
- Building real projects, not just theory
- Asking questions to truly understand
- Making connections to C knowledge

**What I want to improve:**
- Need more practice with lists and tuples (getting there!)
- Want to build more complex projects
- Continue momentum into Week 2

**Key Insight:**
Python makes me productive fast, but C taught me to understand what's happening under the hood. Best of both worlds! 💪

---

*Last updated: Day 6 Complete*