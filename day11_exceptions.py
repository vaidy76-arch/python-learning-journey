"""
Day 11: Error Handling Deep Dive - Exception Types
"""

print("=== Common Exception Types ===\n")

# 1. ValueError - Invalid value for the type
print("1. ValueError - Invalid conversion")
try:
    age = int("twenty")  # Can't convert "twenty" to int
except ValueError as e:
    print(f"   ❌ ValueError: {e}")
    print(f"   Why: String 'twenty' cannot be converted to integer\n")

# 2. TypeError - Wrong type used
print("2. TypeError - Wrong type in operation")
try:
    result = "hello" + 5  # Can't add string and int
except TypeError as e:
    print(f"   ❌ TypeError: {e}")
    print(f"   Why: Cannot concatenate string and integer\n")

# 3. ZeroDivisionError - Division by zero
print("3. ZeroDivisionError - Divide by zero")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"   ❌ ZeroDivisionError: {e}")
    print(f"   Why: Cannot divide by zero\n")

# 4. KeyError - Missing dictionary key
print("4. KeyError - Missing key in dictionary")
try:
    person = {"name": "Alice", "age": 25}
    city = person["city"]  # Key 'city' doesn't exist
except KeyError as e:
    print(f"   ❌ KeyError: {e}")
    print(f"   Why: Key 'city' not found in dictionary\n")

# 5. IndexError - List index out of range
print("5. IndexError - List index out of range")
try:
    numbers = [1, 2, 3]
    value = numbers[10]  # Only 3 items, no index 10
except IndexError as e:
    print(f"   ❌ IndexError: {e}")
    print(f"   Why: List only has 3 items (indices 0-2)\n")

# 6. AttributeError - Object has no attribute
print("6. AttributeError - Missing attribute")
try:
    text = "hello"
    text.append("world")  # Strings don't have append method
except AttributeError as e:
    print(f"   ❌ AttributeError: {e}")
    print(f"   Why: Strings don't have an 'append' method\n")

# 7. NameError - Variable not defined
print("7. NameError - Undefined variable")
try:
    print(undefined_variable)  # Variable doesn't exist
except NameError as e:
    print(f"   ❌ NameError: {e}")
    print(f"   Why: Variable was never created\n")

print("✅ All exception types demonstrated!")


print("\n" + "="*50)
print("=== try/except/else/finally Patterns ===")
print("="*50 + "\n")

# Example 1: Basic try/except
print("--- Example 1: Basic try/except ---")
def divide_basic(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None

print(f"10 / 2 = {divide_basic(10, 2)}")
print(f"10 / 0 = {divide_basic(10, 0)}")

# Example 2: try/except/else
print("\n--- Example 2: try/except/else ---")
def divide_with_else(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero!")
        return None
    else:
        # This ONLY runs if no exception occurred
        print(f"✅ Success: Division completed")
        return result

print(f"Result: {divide_with_else(10, 2)}")
print(f"Result: {divide_with_else(10, 0)}")

# Example 3: try/except/finally
print("\n--- Example 3: try/except/finally ---")
def read_file_safe(filename):
    file = None
    try:
        print(f"Attempting to open {filename}...")
        file = open(filename, "r", encoding="utf-8")  # ← Added encoding!
        content = file.read()
        print(f"✅ File read successfully")
        return content
    except FileNotFoundError:
        print(f"❌ Error: File not found")
        return None
    except UnicodeDecodeError:
        print(f"❌ Error: Cannot decode file")
        return None
    finally:
        # ALWAYS runs - even if exception occurred!
        if file:
            file.close()
            print("🔒 File closed")
        print("✨ Finally block executed\n")

# Test with existing file
read_file_safe("day11_exceptions.py")

# Test with missing file
read_file_safe("missing.txt")


print("\n--- Example 4: Complete Pattern (try/except/else/finally) ---")

def process_user_data(filename):
    """
    Process user data from file with complete error handling.
    Demonstrates all four blocks working together.
    """
    file = None
    processed_count = 0
    
    try:
        print(f"📂 Opening file: {filename}")
        file = open(filename, "r", encoding="utf-8")
        
        print(f"📖 Reading data...")
        lines = file.readlines()
        
        print(f"⚙️  Processing {len(lines)} lines...")
        # Simulate processing (might raise error)
        for line in lines[:5]:  # Process first 5 lines
            processed_count += 1
        
        # This could raise an error (simulate division)
        average = 100 / processed_count
        
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found")
        return None
        
    except ZeroDivisionError:
        print(f"❌ Error: No data to process (division by zero)")
        return None
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None
        
    else:
        # SUCCESS! Only runs if NO exception occurred
        print(f"✅ Success: Processed {processed_count} lines")
        print(f"📊 Average: {average}")
        return processed_count
        
    finally:
        # CLEANUP - Always runs!
        if file and not file.closed:
            file.close()
            print(f"🔒 File closed")
        print(f"✨ Finally block completed")
        print("-" * 50)


# Test 1: Success case
print("\n=== Test 1: Valid file ===")
result = process_user_data("day11_exceptions.py")
print(f"Return value: {result}\n")

# Test 2: Missing file
print("=== Test 2: Missing file ===")
result = process_user_data("nonexistent.txt")
print(f"Return value: {result}\n")

# Test 3: Create empty file (will cause ZeroDivisionError)
print("=== Test 3: Empty file ===")
with open("empty_test.txt", "w", encoding="utf-8") as f:
    f.write("")  # Empty file

result = process_user_data("empty_test.txt")
print(f"Return value: {result}\n")