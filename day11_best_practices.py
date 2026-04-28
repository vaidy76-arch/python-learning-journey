"""
Day 11: Error Handling Best Practices
"""

print("=== Best Practices for Exception Handling ===\n")

# ============================================
# PRACTICE 1: Catch Specific Exceptions
# ============================================
print("--- Practice 1: Catch Specific Exceptions ---\n")

# ❌ BAD - Too broad
print("BAD: Catching everything")
try:
    value = int("not a number")
except Exception:
    print("Something went wrong!")  # What went wrong? We don't know!

# ✅ GOOD - Specific exceptions
print("\nGOOD: Catching specific errors")
try:
    value = int("not a number")
except ValueError:
    print("Invalid number format - please enter digits only")
except TypeError:
    print("Wrong type provided")


# ============================================
# PRACTICE 2: Don't Suppress Errors Silently
# ============================================
print("\n--- Practice 2: Don't Suppress Errors ---\n")

# ❌ BAD - Silent failure
print("BAD: Silent error suppression")
try:
    result = 10 / 0
except:
    pass  # ERROR HIDDEN! No one knows what happened!

print("Code continues... (but error was hidden)")

# ✅ GOOD - At least log the error
print("\nGOOD: Log or handle the error")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error caught and logged: {e}")
    # In production: log to file, send alert, etc.


# ============================================
# PRACTICE 3: Use finally for Cleanup
# ============================================
print("\n--- Practice 3: Use finally for Cleanup ---\n")

# ❌ BAD - Manual cleanup (easy to forget!)
print("BAD: Manual cleanup")
file = open("day11_best_practices.py", "r", encoding="utf-8")
try:
    content = file.read()
    print("File read successfully")
except Exception as e:
    print(f"Error: {e}")
file.close()  # What if exception occurred? File might not close!

# ✅ GOOD - Cleanup in finally
print("\nGOOD: Cleanup in finally block")
file = None
try:
    file = open("day11_best_practices.py", "r", encoding="utf-8")
    content = file.read()
    print("File read successfully")
except Exception as e:
    print(f"Error: {e}")
finally:
    if file:
        file.close()
        print("File closed in finally")

# ✅ BEST - Use context manager (with statement)
print("\nBEST: Use 'with' statement")
try:
    with open("day11_best_practices.py", "r", encoding="utf-8") as f:
        content = f.read()
        print("File read successfully (auto-closes!)")
except Exception as e:
    print(f"Error: {e}")


# ============================================
# PRACTICE 4: Preserve Original Exception
# ============================================
print("\n--- Practice 4: Preserve Original Exception ---\n")

# ❌ BAD - Loses original error info
print("BAD: Losing original error")
def process_data_bad(data):
    try:
        return int(data)
    except ValueError:
        raise Exception("Processing failed")  # Original error lost!

try:
    process_data_bad("abc")
except Exception as e:
    print(f"Error: {e}")  # Can't see it was a ValueError!

# ✅ GOOD - Chain exceptions
print("\nGOOD: Chain exceptions")
def process_data_good(data):
    try:
        return int(data)
    except ValueError as e:
        raise Exception("Processing failed") from e  # Preserves original!

try:
    process_data_good("abc")
except Exception as e:
    print(f"Error: {e}")
    if e.__cause__:
        print(f"  Original cause: {e.__cause__}")


# ============================================
# PRACTICE 5: Order Exceptions Correctly
# ============================================
print("\n--- Practice 5: Order Exceptions (Specific → General) ---\n")

# ❌ BAD - General exception first
print("BAD: General exception catches everything")
try:
    numbers = [1, 2, 3]
    value = numbers[10]
except Exception:
    print("Caught by generic Exception")  # Too broad!
except IndexError:
    print("This will NEVER run!")  # Unreachable code!

# ✅ GOOD - Specific exceptions first
print("\nGOOD: Specific exceptions first")
try:
    numbers = [1, 2, 3]
    value = numbers[10]
except IndexError:
    print("List index out of range - caught by specific exception")
except Exception:
    print("Caught by generic Exception")  # Fallback


# ============================================
# PRACTICE 6: Don't Use Bare except
# ============================================
print("\n--- Practice 6: Avoid Bare 'except:' ---\n")

# ❌ BAD - Bare except catches EVERYTHING
print("BAD: Bare except")
try:
    value = 10 / 0
except:  # Catches even KeyboardInterrupt (Ctrl+C)!
    print("Error occurred")

# ✅ GOOD - At least catch Exception
print("\nGOOD: Catch Exception explicitly")
try:
    value = 10 / 0
except Exception as e:  # Doesn't catch system exits
    print(f"Error: {e}")


# ============================================
# PRACTICE 7: Provide Helpful Error Messages
# ============================================
print("\n--- Practice 7: Helpful Error Messages ---\n")

# ❌ BAD - Vague message
print("BAD: Vague error message")
def divide_bad(a, b):
    if b == 0:
        raise ValueError("Bad value")  # What value? Why bad?
    return a / b

try:
    divide_bad(10, 0)
except ValueError as e:
    print(f"Error: {e}")

# ✅ GOOD - Descriptive message
print("\nGOOD: Descriptive error message")
def divide_good(a, b):
    if b == 0:
        raise ValueError(f"Cannot divide {a} by zero. Divisor must be non-zero.")
    return a / b

try:
    divide_good(10, 0)
except ValueError as e:
    print(f"Error: {e}")


print("\n" + "="*50)
print("✅ Best Practices Review Complete!")
print("="*50)