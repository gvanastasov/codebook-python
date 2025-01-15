# Chapter 16: Working with Dates and Times

"""
Introduction:
In this chapter, we'll explore the `datetime` module, which provides classes for manipulating dates and times. Working with dates and times is essential for tasks like scheduling, logging, and handling time-based events.

Key Concepts:
1. `datetime` Module: A Python module for working with dates and times.
2. `date` and `time` Classes: Represent dates and times separately.
3. `timedelta`: Represents the difference between two `datetime` objects.
4. Formatting Dates: Converting `datetime` objects into readable string formats.
5. Parsing Strings to Dates: Converting strings into `datetime` objects using `strptime()`.

Notes:
- The `datetime` module makes it easy to perform operations like calculating the difference between two dates or converting a date into a string.
- The `timedelta` object is used to perform date and time arithmetic (e.g., adding or subtracting days).

"""

# Program: Calculate the number of days between two dates using the datetime module

import datetime  # Import the datetime module

# Function to calculate the difference between two dates
def calculate_days_between_dates(date1_str, date2_str, date_format="%Y-%m-%d"):
    """Calculate the number of days between two dates in the format YYYY-MM-DD."""
    # Convert the string dates to datetime objects
    date1 = datetime.datetime.strptime(date1_str, date_format)
    date2 = datetime.datetime.strptime(date2_str, date_format)
    
    # Calculate the difference between the two dates
    delta = date2 - date1
    return delta.days

# Example usage
date1 = "2024-01-01"  # Start date
date2 = "2025-01-01"  # End date

# Calculate and print the number of days between the two dates
days_between = calculate_days_between_dates(date1, date2)
print(f"The number of days between {date1} and {date2} is {days_between} days.")

# Current date and time
current_datetime = datetime.datetime.now()  # Get current date and time
print(f"\nCurrent date and time: {current_datetime}")

# Formatting dates into a readable string
formatted_date = current_datetime.strftime("%A, %B %d, %Y")  # Full date format (e.g., Monday, January 01, 2025)
print(f"Formatted date: {formatted_date}")

# Getting just the date (ignoring the time)
current_date = current_datetime.date()
print(f"Today's date: {current_date}")

# Adding days to the current date
future_date = current_datetime + datetime.timedelta(days=100)  # Add 100 days
print(f"Date 100 days from now: {future_date.strftime('%Y-%m-%d')}")

# Subtracting days from the current date
past_date = current_datetime - datetime.timedelta(days=100)  # Subtract 100 days
print(f"Date 100 days ago: {past_date.strftime('%Y-%m-%d')}")
