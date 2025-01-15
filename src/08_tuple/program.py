# Chapter 08: Tuples

"""
Introduction:
Tuples are ordered and immutable collections of elements. 
Once a tuple is created, its values cannot be changed, making tuples ideal for storing fixed sets of data.

Key Concepts:
1. Tuple Creation: Using parentheses `()` to define a tuple.
2. Accessing Elements: Using indexing and slicing to retrieve specific elements.
3. Tuple Immutability: Understanding that tuples cannot be modified after creation.
4. Tuple Unpacking: Assigning tuple elements to individual variables.

Notes:
- Tuples can hold elements of any data type.
- Tuples are zero-indexed (first element at index 0).
- Tuples are useful for fixed collections of data, like coordinates or constants.
"""

# Tuples in Action

# Create a tuple of grades
grades = (85, 90, 78, 92, 88)

# Display the tuple
print("Grades Tuple:", grades)

# Accessing tuple elements
print("First Grade:", grades[0])
print("Last Grade:", grades[-1])

# Tuples are immutable, so the following will cause an error:
# grades[0] = 80  # Uncommenting this line will raise a TypeError

# Tuple unpacking
math, science, english, history, art = grades
print("Unpacked Grades:", math, science, english, history, art)

# Iterating over a tuple
print("\nIterating Over the Tuple:")
for grade in grades:
    print("Grade:", grade)
