# A closure is a function that "remembers" variables from its parent scope

def make_multiplier(n):
    """
    Returns a function that multiplies by n.
    
    The returned function "remembers" n even after make_multiplier finishes!
    """
    # This inner function has access to 'n' from outer function
    def multiplier(x):
        return x * n  # Uses 'n' from parent scope
    
    return multiplier  # Return the function itself (not calling it!)

# Create specialized functions
times_2 = make_multiplier(2)  # Creates function that multiplies by 2
times_5 = make_multiplier(5)  # Creates function that multiplies by 5

# Each function "remembers" its own 'n'
print(times_2(10))  # 10 * 2 = 20
print(times_5(10))  # 10 * 5 = 50

# The magic: 'n' is different for each function!
print(times_2(7))   # 7 * 2 = 14
print(times_5(7))   # 7 * 5 = 35


def create_counter(start=0):
    """
    Create a counter that remembers its count.
    
    Returns a function that increments and returns count each time.
    """
    count = start  # This variable persists!
    
    def increment():
        nonlocal count  # Tell Python we're modifying the outer 'count'
        count += 1
        return count
    
    return increment

# Create two independent counters
counter1 = create_counter(0)
counter2 = create_counter(100)

# Each counter maintains its own count
print(counter1())  # 1
print(counter1())  # 2
print(counter1())  # 3

print(counter2())  # 101
print(counter2())  # 102

print(counter1())  # 4 (still independent!)