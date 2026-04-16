def calculate(operation, *numbers):
    """
    Perform calculation on any number of values.
    
    Args:
        operation: "add", "subtract", "multiply", "divide", or "average"
        *numbers: any number of numeric values
    
    Returns:
        Result of calculation, or error message string
    """
    if not numbers:
        return "Error: No numbers provided"
    
    # Dictionary of operations using lambdas
    operations = {
        "add": lambda nums: sum(nums),
        "average": lambda nums: sum(nums) / len(nums),
    }
    
    # For multiply, we still use a regular function (too complex for lambda)
    if operation == "multiply":
        result = 1
        for n in numbers:
            result *= n
        return result
    
    if operation=="subtract":
        result=numbers[0]
        for num in numbers[1:]:
            result-=num
        return result
    # Check once before the loop
    if operation=="divide":
        if 0 in numbers[1:]:  # Single check for all numbers
            return "Error: Cannot divide by zero"
    
        result = numbers[0]
        for num in numbers[1:]:
            result /= num
        return result

    # Check if operation exists in dictionary
    if operation in operations:
        return operations[operation](numbers)
    
    # If we get here, operation is invalid
    return f"Error: Unknown operation '{operation}'"



print(calculate("add", 5, 3, 2))           # Should be 10
print(calculate("add", 1, 2, 3, 4, 5))     # Should be 15
print(calculate("add", 100)) 
print(calculate("multiply", 10,100,2))
print(calculate("average", 5,5,20))    
print(calculate("subtract", 100, 10, 5))   # Should be 85
print(calculate("subtract", 50, 5, 5, 5))  # Should be 35
print(calculate("subtract", 10))     
print (calculate("divide", 100, 2, 5, 10, 4))
# Error tests
print("\n=== Error Tests ===")
print(calculate("add"))                     # Error: No numbers provided
print(calculate("divide", 100, 0))          # Error: can't divide by 0
print(calculate("divide", 100, 2, 0, 5))    # Error: can't divide by 0
print(calculate("power", 2, 3))             # Error: Unknown operation
print(calculate("divide", 0, 2, 5))         # 0.0 (should work!)