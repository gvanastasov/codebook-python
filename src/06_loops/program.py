# Chapter 06: Loops: for and while

"""
Introduction:
Loops are a fundamental programming construct that allow you to repeat a block of code multiple times. 
This chapter introduces `for` and `while` loops, showing how to use them for iteration, and control their flow with `break` and `continue`.

Key Concepts:
1. `for` Loops: Iterate over a sequence (like a list, string, or range).
2. `while` Loops: Repeat as long as a condition is true.
3. Loop Control: Use `break` to exit a loop early, or `continue` to skip to the next iteration.
4. Nested Loops: A loop inside another loop for handling more complex scenarios.

Notes:
- Use `for` loops when the number of iterations is known or you’re iterating over a collection.
- Use `while` loops when the iterations depend on a condition being met.
- Avoid infinite loops by ensuring `while` conditions eventually become false.

"""

# Program to Generate a Multiplication Table for a Number

# Input: Accept a number from the user
number = int(input("Enter a number to generate its multiplication table: "))
limit = 10  # Define the limit for the multiplication table

# Using a for loop to generate the multiplication table
print(f"\nMultiplication Table for {number} using a for loop:")
for i in range(1, limit + 1):
    print(f"{number} x {i} = {number * i}")

# Using a while loop to generate the multiplication table
print(f"\nMultiplication Table for {number} using a while loop:")
i = 1
while i <= limit:
    print(f"{number} x {i} = {number * i}")
    i += 1

# Loop control: Demonstrating break and continue
print("\nDemonstrating Loop Control:")
for i in range(1, limit + 1):
    if i == 5:
        print("Skipping multiplication with 5 (using continue).")
        continue  # Skip the rest of the loop body for i == 5
    if i == 8:
        print("Stopping the loop at 8 (using break).")
        break  # Exit the loop entirely
    print(f"{number} x {i} = {number * i}")

# Nested Loops Example: Multiplication tables from 1 to 3
print("\nNested Loops: Multiplication Tables from 1 to 3")
for table_number in range(1, 4):  # Outer loop for table numbers
    print(f"\nMultiplication Table for {table_number}:")
    for multiplier in range(1, 11):  # Inner loop for multipliers
        print(f"{table_number} x {multiplier} = {table_number * multiplier}")
