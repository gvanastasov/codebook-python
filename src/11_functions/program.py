# Chapter 11: Functions and Reusability

"""
Introduction:
Functions are reusable blocks of code that perform specific tasks. They help in organizing code, reducing redundancy, and improving readability. This chapter focuses on defining, calling, and using functions in Python to solve problems efficiently.

Key Concepts:
1. Defining Functions: Using the `def` keyword.
2. Parameters and Arguments: Passing data into functions.
3. Return Values: Sending output from functions.
4. Scope: Understanding local and global variables.
5. Reusability: Using functions to avoid repeating code.

Notes:
- Functions make your code modular and easier to debug.
- Use meaningful function names to describe their purpose.
- Parameters allow functions to work with different inputs.
- Return values enable functions to provide results back to the caller.

"""

# Program: Check if a Number is Even or Odd Using a Function

# Define a function to check if a number is even
def is_even(number):
    """
    Determines if a number is even.
    
    Parameters:
        number (int): The number to check.
    
    Returns:
        bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0

# Define a function to print the result
def print_even_odd(number):
    """
    Prints whether a number is even or odd.
    
    Parameters:
        number (int): The number to evaluate.
    """
    if is_even(number):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Input: Get a number from the user
user_number = int(input("Enter a number: "))

# Call the function
print_even_odd(user_number)

# Demonstrating Reusability
print("\nDemonstrating Reusability:")
for num in range(5, 11):  # Test numbers from 5 to 10
    print_even_odd(num)
