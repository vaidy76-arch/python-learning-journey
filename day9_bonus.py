"""
Function Decorators - Advanced Closure Pattern
"""

def log_calls(func):
    """
    Decorator that logs each time a function is called.
    This is a closure that wraps another function!
    """
    call_count = 0
    
    def wrapper(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        print(f"\n📞 Call #{call_count} to {func.__name__}()")
        print(f"   Args: {args}")
        print(f"   Kwargs: {kwargs}")
        
        result = func(*args, **kwargs)
        print(f"   ✅ Result: {result}")
        return result
    
    return wrapper


# Use the @ syntax to apply decorator
@log_calls
def add(a, b):
    """Add two numbers"""
    return a + b

@log_calls
def greet(name, greeting="Hello"):
    """Greet someone"""
    return f"{greeting}, {name}!"


# Test the decorated functions
add(5, 3)
add(10, 2)
greet("Alice")
greet("Bob", greeting="Hi")