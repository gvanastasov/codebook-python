# Chapter 10: Sets

"""
Introduction:
Sets are unordered collections of unique elements in Python. They are useful for storing items without duplicates, 
performing mathematical set operations, and checking membership efficiently.

Key Concepts:
1. Set Creation: Using curly braces `{}` or the `set()` function.
2. Properties of Sets: Unordered, unindexed, and no duplicate values.
3. Set Operations: Union, intersection, difference, and symmetric difference.
4. Modifying Sets: Adding or removing elements using methods like `.add()` and `.remove()`.

Notes:
- Sets do not allow duplicates. If duplicates are added, they are automatically removed.
- Sets are unordered, so the elements have no defined order and cannot be accessed by index.
- Use `frozenset` for immutable sets if you need a set to be unmodifiable.
"""

# Program to Find Common and Unique Items Between Two Sets

# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

# Perform set operations
union_set = set1 | set2  # Union: All unique elements from both sets
intersection_set = set1 & set2  # Intersection: Common elements
difference_set = set1 - set2  # Difference: Elements in set1 but not in set2
symmetric_difference_set = set1 ^ set2  # Symmetric Difference: Elements in either set but not both

# Display results
print("\nSet Operations:")
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (Set1 - Set2):", difference_set)
print("Symmetric Difference:", symmetric_difference_set)

# Modify a set
print("\nModifying Sets:")
set1.add(10)  # Add an element to the set
print("After Adding 10 to Set1:", set1)

set2.remove(4)  # Remove an element from the set
print("After Removing 4 from Set2:", set2)

# Check membership
print("\nMembership Testing:")
print("Is 5 in Set1?", 5 in set1)
print("Is 15 in Set2?", 15 in set2)
