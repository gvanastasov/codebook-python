# Chapter 17: Regular Expressions (Regex)

"""
Introduction:
Regular expressions (regex) are a powerful tool in Python for pattern matching in strings. They allow you to search for, match, and manipulate strings in complex ways. In this chapter, we'll explore how to use the `re` module to perform pattern matching and validate inputs such as email addresses.

Key Concepts:
1. `re` Module: The built-in module for working with regular expressions.
2. Patterns: Regex patterns to match specific string formats.
3. Special Characters: Symbols such as `\d`, `\w`, `+`, `*`, etc., used to define patterns.
4. Groups: Parentheses `()` used to capture parts of a match for further processing.

Notes:
- Regular expressions are widely used for string validation, searching, and replacement.
- The `re` module provides functions like `re.match()`, `re.search()`, `re.findall()`, and `re.sub()` to work with regex patterns.

"""

# Program: Validate email addresses using regular expressions

import re  # Import the re module for regular expressions

# Function to validate an email address
def validate_email(email):
    """Check if the provided email is in a valid format."""
    # Define the regular expression pattern for a valid email
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Use re.match to see if the email matches the pattern
    if re.match(email_pattern, email):
        return True
    else:
        return False

# Example usage
emails = [
    "test@example.com",  # Valid email
    "invalid-email",     # Invalid email
    "user@domain.co.uk", # Valid email
    "hello@world",       # Invalid email
]

for email in emails:
    if validate_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")

# Explanation of the Regex Pattern
# The pattern used for matching emails is:
# ^                    : Matches the start of the string.
# [a-zA-Z0-9_.+-]+      : Matches one or more characters that are letters, digits, or special characters allowed in the local part of the email.
# @                    : Matches the literal "@" symbol.
# [a-zA-Z0-9-]+         : Matches one or more characters that are letters, digits, or hyphens in the domain part.
# \.                   : Matches the literal dot (.) in the domain.
# [a-zA-Z0-9-.]+       : Matches one or more characters that are letters, digits, hyphens, or dots in the domain suffix.
# $                    : Matches the end of the string.

