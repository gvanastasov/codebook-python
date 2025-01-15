# Chapter 04: Strings and Basic Manipulations

"""
Introduction:
This chapter introduces strings, one of the most versatile and commonly used data types in Python. 
You'll learn how to create and manipulate strings using slicing, methods, and formatting. 
Strings are sequences of characters, making them easy to access, modify, and analyze.

Key Concepts:
1. String Slicing: Extract specific parts of a string using index ranges.
2. String Methods: Use built-in methods to modify or analyze strings.
3. String Formatting: Combine strings with variables for dynamic output.

Notes:
- Strings in Python are immutable, meaning their contents cannot be changed after creation.
- Indexing starts at 0, and negative indices access elements from the end of the string.
- Use `str` methods like `.lower()`, `.upper()`, `.strip()`, `.replace()`, etc., for common operations.
"""

# Strings and Basic Manipulations in Action

# Declare and display a string
original_string = "Madam"
print("Original String:", original_string)

# String slicing
first_char = original_string[0]  # First character
last_char = original_string[-1]  # Last character
middle_slice = original_string[1:-1]  # Middle part of the string

print("First Character:", first_char)
print("Last Character:", last_char)
print("Middle Slice:", middle_slice)

# Reverse the string using slicing
reversed_string = original_string[::-1]
print("Reversed String:", reversed_string)

# Check if the string is a palindrome (same forwards and backwards)
is_palindrome = original_string.lower() == reversed_string.lower()
print(f"Is '{original_string}' a palindrome?: {is_palindrome}")

# String methods
print("\nString Methods:")
lowercase = original_string.lower()  # Convert to lowercase
uppercase = original_string.upper()  # Convert to uppercase
replaced_string = original_string.replace("a", "@")  # Replace 'a' with '@'

print("Lowercase:", lowercase)
print("Uppercase:", uppercase)
print("Replaced String:", replaced_string)

# String formatting
name = "Alice"
message = f"Hello, {name}! Did you know '{original_string}' is a palindrome?: {is_palindrome}"
print("\nFormatted Message:", message)

# User input example
print("\nUser Input:")
user_string = input("Enter a word to check if it’s a palindrome: ")
is_user_palindrome = user_string.lower() == user_string[::-1].lower()
print(f"Is '{user_string}' a palindrome?: {is_user_palindrome}")
