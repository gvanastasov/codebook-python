# Chapter 07: Lists

"""
Introduction:
Lists are ordered and mutable collections of elements. They are one of the most versatile data structures in Python. 
You can add, remove, and modify elements in a list, making them suitable for a wide range of tasks.

Key Concepts:
1. List Creation: Using square brackets `[]` to define a list.
2. Indexing and Slicing: Accessing individual elements or subsets of a list.
3. List Methods: Built-in functions to manipulate and analyze lists.
4. Iterating Over Lists: Using loops to process each element.

Notes:
- Lists can hold elements of any data type.
- Lists are zero-indexed (first element at index 0).
- Lists are mutable, allowing modifications after creation.
"""

# Program to Find the Average, Maximum, and Minimum of Numbers in a List

# Create a list of numbers
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Display the list
print("Numbers List:", numbers)

# Calculate average, maximum, and minimum
average = sum(numbers) / len(numbers)
maximum = max(numbers)
minimum = min(numbers)

print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")

# Indexing and Slicing
print("\nIndexing and Slicing Examples:")
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])
print("Middle Elements (2nd to 5th):", numbers[1:5])  # Slicing from index 1 to 4

# Using List Methods
print("\nUsing List Methods:")
numbers.append(110)  # Add a new element to the end
print("After Append:", numbers)

numbers.remove(50)  # Remove the element 50
print("After Removing 50:", numbers)

numbers.sort(reverse=True)  # Sort in descending order
print("After Sorting Descending:", numbers)
