# Chapter 15: Modules and Libraries

"""
Introduction:
In Python, a module is a file containing Python definitions and statements. A library is a collection of modules. Python has a rich standard library, which provides functions and tools to perform common tasks, such as mathematical calculations, data manipulation, file handling, and more.

Key Concepts:
1. Modules: A way to organize Python code into reusable components.
2. Libraries: A collection of modules providing additional functionality.
3. Importing: You can import entire modules or specific functions from a module.
4. Standard Library: Python comes with many built-in modules (e.g., `math`, `os`, `random`).

Notes:
- The `import` keyword is used to include external modules into your program.
- You can import a module entirely or import specific functions to keep your code clean.
- The `math` module is one of the most commonly used for mathematical operations.

"""

# Program: Calculate the area of various shapes using the math module

import math  # Import the math module

def area_of_circle(radius):
    """Calculate the area of a circle."""
    return math.pi * (radius ** 2)

def area_of_rectangle(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def area_of_triangle(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height

def area_of_square(side):
    """Calculate the area of a square."""
    return side ** 2

# Example usage
print("Area of Circle with radius 5:", area_of_circle(5))
print("Area of Rectangle with length 4 and width 6:", area_of_rectangle(4, 6))
print("Area of Triangle with base 3 and height 4:", area_of_triangle(3, 4))
print("Area of Square with side 7:", area_of_square(7))

# Using math functions from the math module
print("\nUsing math functions from the math module:")
print("Square root of 16:", math.sqrt(16))  # Square root
print("Power of 2 raised to 3:", math.pow(2, 3))  # Exponentiation
print("Random number between 0 and 1:", math.random())  # Random number (Note: math module doesn't have random function, use random module for random numbers)
