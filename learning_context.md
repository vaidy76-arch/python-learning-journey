Teaching style: STEP-BY-STEP INTERACTIVE (NOT information dumps)

## Teaching style preference - CRITICAL RULES

**NEVER dump all information at once. Always go step-by-step and wait for confirmation.**

### Structure for Each Day:
1. **Concept Overview** (5 min) - Brief intro only
2. **Step-by-step teaching** - ONE step at a time
   - Present Step N with time estimate
   - Explain the concept BEFORE code
   - Show ONLY the code for that step
   - Wait for "ready" or "let's go" before next step
   - NEVER show all steps at once

### For Each Step:
- Numbered steps with time estimates (Step 1: 5 min, Step 2: 10 min)
- Explain concept BEFORE showing code
- Detailed line-by-line explanations for new code
- Ask "Ready for Step N?" and WAIT for response
- Let me try things myself when I want to

### Practice Exercises:
- Build together step-by-step
- Ask "Ready for Step N?" between each part
- Let me share my code for review
- Don't show full solution upfront
- Provide starter templates (not blank files)

### What NOT to do:
- ❌ Don't give all steps/code at once
- ❌ Don't show complete solutions before I try
- ❌ Don't move ahead without confirmation
- ❌ Don't assume I'm ready for next step
- ❌ Don't dump entire practice exercise solution

### What TO do:
- ✅ One step at a time
- ✅ Wait for "yes, let's go" or "I'm ready"
- ✅ Let me try things and share my code
- ✅ Detailed explanations for each new line
- ✅ Starter templates when needed
- ✅ Checklist at end of each day
- ✅ Git commit steps included
- ✅ Bonus challenge (optional) offered at end

### Example Good Flow:
Claude: "Step 1: Setup (2 min). Create file and add this..."
Vaidy: [does it] "done"
Claude: "Great! Ready for Step 2?"
Vaidy: "yes"
Claude: "Step 2: Add validation (3 min). Now we'll..."
[explains concept, shows code for Step 2 only]
Vaidy: [does it] "ready"
Claude: "Perfect! Ready for Step 3?"

### Example Bad Flow (DON'T DO THIS):
Claude: [dumps Steps 1-6 all at once with all code]
Vaidy: "too much, can't follow"

**Key principle: Interactive and paced, not information dump**

---
# 6-Month Full Stack Learning Plan

## Stack: Python → Flask → React
## Daily commitment: 1 hour/day
## Start date: December 2024

---

## Month 1: Python Fundamentals & Backend Basics

### Week 1: Python Core (Days 1-7)
- Day 1: Environment setup (Python, VS Code, Git, venv, GitHub)
- Day 2: Variables, data types, string operations, calculator
- Day 3: Control flow (if/elif/else), guessing game, rock paper scissors
- Day 4: Loops (for/while, break/continue, enumerate), patterns, shopping cart
- Day 5: Lists, tuples, list comprehensions, JSON file I/O, todo manager
- Day 6: Functions, modules, *args/**kwargs, docstrings, custom modules
- Day 7: Review + Capstone (Personal Finance Tracker + Contact Manager)

### Week 2: OOP & Advanced Functions (Days 8-14)
- Day 8: Classes, objects, __init__, self, magic methods ✅
- Day 9: Advanced functions (*args, **kwargs, lambda, closures)
- Day 10: File operations (read/write, CSV, JSON, error handling)
- Day 11: Error handling (try/except/finally, custom exceptions)
- Day 12: Modules & packages (os, sys, datetime, json, custom modules)
- Day 13: OOP Part 2 (inheritance, polymorphism, method overriding)
- Day 14: OOP Part 3 + Week review (abstract classes, composition)

### Week 3: Git, HTTP & Flask Intro (Days 15-21)
- Day 15: Git deep dive (branching, merging, conflicts, PRs)
- Day 16: HTTP & web fundamentals (GET/POST/PUT/DELETE, status codes, REST)
- Day 17: Working with APIs (requests library, OpenWeatherMap)
- Day 18: More API practice (POST requests, auth, API keys)
- Day 19: Virtual environments & dependencies (venv, requirements.txt, pip)
- Day 20: Flask intro (routes, decorators, dev server)
- Day 21: Flask basics continued (URL params, JSON responses, multiple routes)

### Week 4: Building Your First API (Days 22-28)
- Day 22: Flask request handling (request object, POST, JSON body)
- Day 23: In-memory data storage (Task API - create, read)
- Day 24: Complete CRUD (PUT, DELETE endpoints, test with Postman)
- Day 25: API organization (blueprints, error handling, status codes)
- Day 26: SQL intro (PostgreSQL/SQLite, CREATE, INSERT, SELECT)
- Day 27: SQL continued (UPDATE, DELETE, JOINs, DBeaver/pgAdmin)
- Day 28: Month 1 Capstone — Task Manager API with JSON storage

---

## Month 2: Databases & Advanced Flask

### Week 5-6: PostgreSQL & SQLAlchemy
- PostgreSQL deep dive (indexes, transactions, relationships)
- SQLAlchemy ORM (models, queries, migrations)
- Flask-SQLAlchemy integration
- Database design (one-to-many, many-to-many relationships)
- Alembic migrations
- Practice: Blog API with users, posts, comments

### Week 7-8: Authentication & Advanced Flask
- User authentication (password hashing with bcrypt)
- JWT tokens (PyJWT, access/refresh tokens)
- Session management
- Flask blueprints for large apps
- Input validation (Flask-WTF, marshmallow)
- Environment variables & config management
- Practice: Full auth system with registration, login, protected routes

---

## Month 3: Frontend Basics & JavaScript

### Week 9-10: HTML, CSS, JavaScript Fundamentals
- HTML semantics, forms, accessibility basics
- CSS flexbox, grid, responsive design
- JavaScript ES6+: variables, functions, arrays, objects
- DOM manipulation and event handling
- Fetch API for HTTP requests
- Practice: Interactive pages that call your Flask API

### Week 11-12: Modern Frontend
- React intro (components, JSX, props)
- React hooks (useState, useEffect)
- React Router (navigation, URL params)
- Axios for API calls
- Tailwind CSS for styling
- Practice: Task manager UI connected to Flask API

---

## Month 4: Full Stack Integration

### Week 13-14: Connecting Frontend & Backend
- CORS handling in Flask
- React Query or SWR for data fetching
- Loading states and error handling in UI
- Form handling in React
- Authentication flow (login, JWT storage, protected routes)
- Practice: Wire Month 3 React app to Month 2 Flask API

### Week 15-16: Advanced Full Stack
- File uploads (Flask + React)
- Real-time features intro (Flask-SocketIO)
- Pagination (backend + frontend)
- Search functionality
- API rate limiting
- Practice: Full stack blog platform with auth

---

## Month 5: Deployment & Real-World Skills

### Week 17-18: Deploy & DevOps Basics
- Docker basics (Dockerfile, docker-compose)
- Deploy Flask backend to Render or Railway
- Deploy React frontend to Vercel or Netlify
- GitHub Actions CI/CD pipeline
- Environment variables in production
- HTTPS and domain setup
- Practice: Ship your full stack app publicly

### Week 19-20: Testing & Code Quality
- pytest for Python (unit tests, fixtures, mocking)
- Integration tests for Flask APIs
- React testing basics (Vitest)
- Code review practices
- Linting (flake8, ESLint)
- Practice: Add tests to existing projects

---

## Month 6: Portfolio & Job Readiness

### Week 21-22: Capstone Projects
- Project 1: E-commerce site or blog platform
- Project 2: Real-time chat application (Flask-SocketIO + React)
- Project 3: Something from your own domain (CSV/Excel automation tool?)
- Each project: Full stack, deployed, with tests, clean README

### Week 23-24: Job Readiness
- TypeScript basics
- System design fundamentals
- Portfolio site (showcase all projects)
- GitHub profile cleanup
- LeetCode Easy/Medium problems
- Contribute to one open source project
- Interview prep (common Python/JS questions)

---

## Daily Session Structure (1 hour)
- Minutes 0-15: Review previous day's concepts
- Minutes 15-40: New material (tutorial/reading)  
- Minutes 40-55: Hands-on coding practice
- Minutes 55-60: Git commit + update learning journal

## Weekly Structure
- Weekdays: 1 hour structured learning
- Weekends: Longer project sessions, code review, reading

---

## Resources
- Python: Real Python (realpython.com), official docs
- Flask: flask.palletsprojects.com
- JavaScript: MDN Web Docs
- React: react.dev (official docs)
- SQL: pgexercises.com for practice
- Deployment: render.com, railway.app, vercel.com
- API Testing: Postman
- SQL Client: DBeaver

---

## Key Rules
1. Build every day — even 30 minutes counts
2. Push to GitHub daily — your portfolio grows automatically
3. Stuck for 20 minutes? Move on, come back later
4. Master one thing at a time — don't chase every framework
5. Projects > tutorials — always be building something

---

## Success Milestones
- End of Month 1: Working REST API, solid Python, basic SQL
- End of Month 2: Full auth system, database-backed API
- End of Month 3: React app talking to your own API
- End of Month 4: Complete full stack app running locally
- End of Month 5: App deployed live with tests
- End of Month 6: 3 deployed projects + portfolio site + job ready

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
# 📇 Contact Management System

A command-line application to manage your contacts efficiently, built with Python.

## Features

- ✅ Add new contacts (name, phone, email, address)
- ✅ View all contacts in a formatted table (sorted alphabetically)
- ✅ Search contacts by name (partial match, case-insensitive)
- ✅ Edit contact details (any field)
- ✅ Delete contacts with confirmation
- ✅ Data persistence (auto-save to JSON)
- ✅ Automatic data loading on startup
- ✅ Input validation and error handling
- ✅ Clean, interactive menu interface

## Technologies Used

- Python 3.11+
- JSON for data storage
- datetime module for timestamps
- Modular design with separate function library

## Project Structure

contact_manager/
├── contact_functions.py  
├── main.py              
├── contacts.json        
└── README.md           

## How to Run

1. Make sure Python 3.11+ is installed
2. Navigate to the contact_manager folder:
```bash
   cd contact_manager
```
3. Run the program:
```bash
   python main.py
```

## Usage

### Main Menu Options:

Add New Contact     - Create a new contact entry
View All Contacts   - Display all contacts in sorted table
Search Contact      - Find contacts by name (partial match)
Edit Contact        - Update any contact field
Delete Contact      - Remove a contact (with confirmation)
Save & Exit         - Save data and quit application

### Sample Workflow:

Add Contact:

Name: Alice Johnson
Phone: 555-1234
Email: alice@email.com
Address: 123 Main St


View All → See Alice in the list
Search "ali" → Finds Alice
Edit Alice → Change phone to 555-0000
Delete Alice → Confirms and removes
Exit → Data automatically saves to JSON

## Data Storage

Contacts are stored in `contacts.json` with this structure:

```json
[
  {
    "id": 1,
    "name": "Alice Johnson",
    "phone": "555-1234",
    "email": "alice@email.com",
    "address": "123 Main St",
    "groups": [],
    "date": "2024-12-15"
  }
]
```

## Functions Module (`contact_functions.py`)

### Core Functions:

- `load_contacts()` - Load contacts from JSON file
- `save_contacts()` - Save contacts to JSON file
- `get_next_id()` - Generate unique contact IDs
- `add_contact()` - Create new contact with duplicate checking
- `view_all_contacts()` - Display formatted table (sorted alphabetically)
- `search_contact()` - Find contacts by name (partial, case-insensitive)
- `edit_contact()` - Update contact fields dynamically
- `delete_contact()` - Remove contact with confirmation

### Key Features:

- **Dynamic field editing**: Automatically adapts to new fields
- **System fields protection**: ID, date, and groups cannot be edited
- **Duplicate prevention**: Checks for existing names before adding
- **Error handling**: Graceful handling of missing files and corrupted data

## Error Handling

The application handles:
- ❌ Missing data file (starts fresh)
- ❌ Corrupted JSON data (notifies user)
- ❌ Invalid user input (validates numbers)
- ❌ Duplicate contacts (prevents creation)
- ❌ Contact not found (appropriate messages)

## Design Decisions

### Why Separate Modules?

- **contact_functions.py**: Pure business logic, reusable functions
- **main.py**: UI/menu logic, user interaction

This separation allows:
- ✅ Easy testing of functions independently
- ✅ Reusable code for other interfaces (GUI, web, etc.)
- ✅ Clear organization and maintainability

### Dynamic Field Detection

```python
SYSTEM_FIELDS = ['id', 'date', 'groups']
editable_fields = [key for key in contact.keys() if key not in SYSTEM_FIELDS]
```

This approach:
- ✅ Automatically includes new fields when added
- ✅ No hardcoded field lists to maintain
- ✅ Future-proof design

## Future Enhancements

Possible improvements:
- [ ] Input validation (phone format, email format)
- [ ] Group management (Family, Work, Friends)
- [ ] Export to CSV
- [ ] Import from CSV
- [ ] Edit/delete multiple contacts
- [ ] Backup/restore functionality
- [ ] Advanced search (by phone, email, etc.)
- [ ] Contact photos
- [ ] GUI interface (Tkinter or web-based)

## What I Learned

This project helped me practice:
- ✅ Functions and modular code organization
- ✅ Working with JSON files (read/write)
- ✅ Exception handling (try/except)
- ✅ List comprehensions and lambda functions
- ✅ String formatting and tables
- ✅ User input validation
- ✅ Dictionary manipulation
- ✅ Code reusability
- ✅ Separation of concerns (UI vs logic)

## Testing

To test the functions independently:

```bash
python contact_functions.py
```

This runs built-in test cases that verify:
- Adding contacts
- Duplicate detection
- Save/load functionality

## Author

Built as capstone project for Week 1 of Python learning journey (Day 7).

**Date:** December 2024  
**Time invested:** ~3-4 hours  
**Lines of code:** ~250+

---

*Second capstone project of Week 1 - Part of my 6-month journey to become a full-stack developer* 🚀

## Acknowledgments

- Built alongside Personal Finance Tracker (first capstone project)
- Demonstrates mastery of Week 1 concepts: variables, control flow, loops, functions, modules, file I/O

Current day: Day 8 - OOP (COMPLETED)
Concepts covered:
  - Classes and objects (__init__, self, methods)
  - Class vs instance attributes
  - Magic methods (__str__, __eq__, __add__)
  - return vs print distinction

Files created: day8_classes.py, day8_practice.py
Projects: Book class with read/progress tracking

Key lessons learned:
  - self = this specific object
  - Class attributes shared, instance attributes unique
  - Magic methods triggered by operators, not called directly
  - return sends value back, print shows it on screen

Next: Day 9 - Advanced functions (*args, **kwargs, lambda)

Current day: Day 8 - OOP (COMPLETED)
Concepts covered:
  - Classes and objects (__init__, self, methods)
  - Class vs instance attributes
  - Magic methods (__str__, __eq__, __add__)
  - return vs print distinction

Files created: day8_classes.py, day8_practice.py
Projects: Book class with read/progress tracking

Key lessons learned:
  - self = this specific object
  - Class attributes shared, instance attributes unique
  - Magic methods triggered by operators, not called directly
  - return sends value back, print shows it on screen

Next: Day 9 - Advanced functions (*args, **kwargs, lambda)
I'm learning Python, Day 9 of my plan.
Teaching style I prefer:
- Explain every line of new code as we type it
- Don't assume I know why something works
- Give detailed explanations, not just "add this"
Here's my context: [paste learning_context.md]


## Teaching style preference
- Numbered steps with time estimates (Step 1: 5 min, Step 2: 15 min etc.)
- Explain concept before showing code
- Starter templates for practice exercises, not blank files
- Checklist at end of each day
- Bonus challenge after main task
- Git commit steps included in each day
- Detailed line-by-line explanations for new concepts


### Day 9: Advanced Functions (PARTIAL - In Progress)
**Date Completed:** 04/13/2026

**What I Learned:**
- *args collects extra positional arguments into a tuple
- **kwargs collects extra keyword arguments into a dictionary
- Parameter order MUST be: required → *args → defaults → **kwargs
- Lambda functions are one-line anonymous functions
- Used lambda with sorted(), filter(), map()

**Key Concepts:**
- `*args` is greedy - takes ALL extra positional arguments
- `**kwargs` is greedy - takes ALL extra keyword arguments  
- Lambda syntax: `lambda parameters: expression`
- Can't use statements in lambda, only expressions
- Ternary operator: `value_if_true if condition else value_if_false`

**Projects/Files:**
- day9_args.py - *args and **kwargs examples
- day9_lambda.py - Lambda functions and practical uses

**Questions Answered:**
- Q: How does Python assign arguments to *args vs **kwargs?
- A: Positional args (no name=) go to *args, keyword args (with name=) go to **kwargs or matching parameters

**Still To Learn:**
- Closures (tomorrow)
- nonlocal keyword
- Practice calculator exercise
- Function decorators

**Next:** Continue Day 9 - Closures and practice

### Day 9: Advanced Functions ✅
**Date Completed:** 04/15/2026

**What I Learned:**
- *args collects positional arguments into tuple
- **kwargs collects keyword arguments into dictionary
- Parameter order: required → *args → defaults → **kwargs
- Lambda syntax: `lambda params: expression`
- Closures capture variables from parent scope
- nonlocal needed to modify outer scope variables

**Projects Built:**
- Flexible calculator with *args
- Supports: add, multiply, subtract, divide, average
- Error handling for zero division and invalid operations

**Files Created:**
- day9_args.py
- day9_lambda.py
- day9_closures.py
- day9_practice.py

**Key Realizations:**
- Lambda great for quick operations with sorted(), filter(), map()
- Closures better than global variables for encapsulation
- *args is greedy - takes all extra positionals
- Dictionary + lambda = clean, extensible code

**Next:** Day 9 Bonus (decorators) + Day 10 (File operations)

**Current progress:** Week 2, Day 2/7 complete