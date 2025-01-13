# Chapter 03: Basic Arithmetic and Operators

"""
Introduction:
This chapter explores basic arithmetic operations and operators in Python, which are essential for performing mathematical calculations and manipulating data. 
You'll learn about different types of operators, their usage, and how to combine them with variables.

Key Concepts:
1. Arithmetic Operators: Perform basic math operations (e.g., +, -, *, /, //, %, **).
2. Assignment Operators: Assign values to variables (e.g., =, +=, -=, *=, /=).
3. Precedence and Associativity: The rules that determine the order in which operations are performed.

Notes:
- Python uses standard mathematical operators for calculations.
- Division (`/`) always returns a float, even if the result is a whole number.
- Floor division (`//`) returns an integer by discarding the decimal part.
- The modulo operator (`%`) finds the remainder of division.
- Exponentiation (`**`) raises a number to a power.
"""

# Arithmetic and Operators in Action

# Declare variables
a = 10  # Integer
b = 3   # Integer

# Perform arithmetic operations
sum_result = a + b  # Addition
diff_result = a - b  # Subtraction
prod_result = a * b  # Multiplication
div_result = a / b  # Division (returns float)
floor_div_result = a // b  # Floor division (returns integer)
mod_result = a % b  # Modulo (remainder)
exp_result = a ** b  # Exponentiation (a raised to the power of b)

# Display results
print("Arithmetic Operations:")
print(f"Addition: {a} + {b} = {sum_result}")
print(f"Subtraction: {a} - {b} = {diff_result}")
print(f"Multiplication: {a} * {b} = {prod_result}")
print(f"Division: {a} / {b} = {div_result}")
print(f"Floor Division: {a} // {b} = {floor_div_result}")
print(f"Modulo: {a} % {b} = {mod_result}")
print(f"Exponentiation: {a} ** {b} = {exp_result}")

# Assignment operators
print("\nAssignment Operations:")
c = 5  # Assign initial value
print("Initial value of c:", c)

c += 2  # Equivalent to c = c + 2
print("After c += 2:", c)

c *= 3  # Equivalent to c = c * 3
print("After c *= 3:", c)

c -= 1  # Equivalent to c = c - 1
print("After c -= 1:", c)

# Order of operations (precedence and associativity)
print("\nOrder of Operations:")
expr_result = a + b * c - b / a  # Precedence: Multiplication and Division before Addition and Subtraction
print(f"Expression Result: {a} + {b} * {c} - {b} / {a} = {expr_result}")

# User input and arithmetic
print("\nUser Input Arithmetic:")
x = float(input("Enter the first number (x): "))  # Accept user input (float)
y = float(input("Enter the second number (y): "))  # Accept user input (float)

sum_xy = x + y
print(f"The sum of {x} and {y} is {sum_xy}")
