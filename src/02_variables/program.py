# Chapter 02: Variables and Data Types

"""
Introduction:
This chapter introduces variables and data types, fundamental concepts in Python programming. 
You'll learn how to create variables, understand their data types, and see how Python handles text (strings), 
numbers (integers and floats), and user input.

Key Concepts:
1. Variables: Named containers for storing data values.
2. Data Types: Determine the kind of data a variable can hold (e.g., integers, floats, strings).
3. Input and Type Conversion: Using the `input()` function and converting input to the desired data type.

Notes:
- Variables must be declared before use.
- Python is dynamically typed, so you don't need to specify the data type.
- Variables are case-sensitive (e.g., 'age' and 'Age' are different variables).
- Variables can be reassigned with a new value of the same or different data type.

"""

# Variables and Data Types in Action

# Declare variables with different data types
name = "Alice"  # String
age = 30  # Integer
height = 5.7  # Float
is_student = False  # Boolean
complex_number = 3 + 4j  # Complex number (real and imaginary parts)
hobbies = ["reading", "hiking", "coding"]  # List
address = ("123 Main St", "Springfield", "USA")  # Tuple
grades = {"math": 90, "science": 85, "english": 88}  # Dictionary
unique_numbers = {1, 2, 3, 4, 5}  # Set
frozen_unique_numbers = frozenset([1, 2, 3, 4, 5])  # Frozen set
nothing = None  # NoneType

# Print variable values and their types
print("Program Name:", name)  # Displays the name of the program
print("Data type of 'name':", type(name))  # Check the type of 'name'

# Accept user input and convert to appropriate data types
age = int(input("\nEnter your age (an integer): "))

# Display input values and their types
print("Age:", age, "of type", type(age))
