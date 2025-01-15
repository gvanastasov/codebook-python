# Chapter 05: Control Flow: if, elif, and else

"""
Introduction:
Control flow allows you to direct the execution of your program based on conditions. 
This chapter covers conditional statements in Python, including `if`, `elif`, and `else`, which let your program make decisions.

Key Concepts:
1. Boolean Expressions: Logical expressions that evaluate to `True` or `False`.
2. `if` Statement: Executes code when a condition is `True`.
3. `elif` (Else-If): Checks additional conditions if the previous `if` was `False`.
4. `else`: Executes code when all previous conditions are `False`.

Notes:
- Conditions use comparison operators like `==`, `!=`, `<`, `>`, `<=`, and `>=`.
- Logical operators (`and`, `or`, `not`) combine multiple conditions.
- Indentation is crucial in Python; ensure consistent spacing for block structures.

"""

# Conditional Statements in Action

# Program to determine if a number is positive, negative, or zero

# Accept user input and convert to a number
number = float(input("Enter a number: "))

# Conditional statements
if number > 0:
    print(f"{number} is a positive number.")  # Executed if the number is greater than 0
elif number < 0:
    print(f"{number} is a negative number.")  # Executed if the number is less than 0
else:
    print("The number is zero.")  # Executed if the number is exactly 0

# Additional examples of control flow
print("\nMore Examples:")

# Check if a number is even or odd
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# Nested conditions
if number > 0:
    if number > 100:
        print(f"{number} is a large positive number.")
    else:
        print(f"{number} is a small positive number.")
elif number < 0:
    if number < -100:
        print(f"{number} is a large negative number.")
    else:
        print(f"{number} is a small negative number.")
else:
    print("Zero is neither positive nor negative.")

# Logical operators example
print("\nUsing Logical Operators:")
if number > 0 and number % 2 == 0:
    print(f"{number} is a positive and even number.")
elif number > 0 and number % 2 != 0:
    print(f"{number} is a positive and odd number.")
elif number < 0 and abs(number) > 100:
    print(f"{number} is a large negative number.")
else:
    print("No special condition met.")
