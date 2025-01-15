# Chapter 12: Error Handling with try and except

"""
Introduction:
Errors and exceptions are common in programming. Python provides a robust mechanism to handle them using `try` and `except` blocks. 
This ensures your program can handle unexpected situations gracefully without crashing.

Key Concepts:
1. try and except: Catch and handle exceptions.
2. Multiple except Blocks: Handle different types of exceptions separately.
3. finally: Execute cleanup code regardless of exceptions.
4. Raising Exceptions: Manually trigger exceptions with `raise`.

Notes:
- Exceptions are Python's way of indicating errors during runtime (e.g., dividing by zero or accessing a missing file).
- Use `try` blocks to test code that might fail and `except` to handle the failure.
- The `finally` block is optional and is executed no matter what happens.

"""

# Program: Safe Division with Error Handling

def safe_division(num1, num2):
    """
    Performs division and handles potential errors.
    
    Parameters:
        num1 (float): The numerator.
        num2 (float): The denominator.
    
    Returns:
        float or None: The result of the division, or None if an error occurred.
    """
    try:
        # Attempt the division
        result = num1 / num2
    except ZeroDivisionError:
        # Handle division by zero
        print("Error: Cannot divide by zero.")
        result = None
    except TypeError:
        # Handle invalid input types
        print("Error: Both inputs must be numbers.")
        result = None
    else:
        # No errors occurred
        print("Division successful!")
    finally:
        # Code to execute regardless of the result
        print("Execution of safe_division completed.")
    return result

# Input: Get two numbers from the user
try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
except ValueError:
    print("Error: Please enter valid numeric inputs.")
else:
    # Perform safe division
    result = safe_division(numerator, denominator)
    if result is not None:
        print(f"Result: {result}")
