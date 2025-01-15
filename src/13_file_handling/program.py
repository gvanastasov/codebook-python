# Chapter 13: File Handling

import os

"""
Introduction:
File handling allows programs to read from and write to files on your system. This is essential for working with data storage, logging, and configuration files. Python provides a simple and flexible interface for file operations.

Key Concepts:
1. File Modes: Specify how the file should be opened (read, write, append, etc.).
2. Reading Files: Using methods like `.read()`, `.readline()`, and `.readlines()`.
3. Writing Files: Using `.write()` to save data to a file.
4. Appending to Files: Adding data to the end of an existing file.
5. Closing Files: Ensuring files are properly closed after use.

Notes:
- Always close files after working with them to release system resources.
- Use `with open()` for automatic file closing (best practice).
- File modes:
  - `'r'`: Read-only mode (default).
  - `'w'`: Write mode (overwrites the file if it exists).
  - `'a'`: Append mode (adds data to the end of the file).
  - `'r+'`: Read and write mode.

"""

# Program: Create, Write to, Read, and Append to a File

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(script_dir, "example.txt")

# Create and write to a file
with open(file_name, 'w') as file:
    file.write("Welcome to File Handling in Python.\n")
    file.write("This is a new file created using Python.\n")


print(f"Data written to {file_name} successfully.")

# Read the file content
print("\nReading file content:")
with open(file_name, 'r') as file:
    content = file.read()
    print(content)

# Append new data to the file
with open(file_name, 'a') as file:
    file.write("Appending new data to the file.\n")
    file.write("File handling is an essential skill.\n")

print(f"\nNew data appended to {file_name}.")

# Read the updated file content
print("\nReading updated file content:")
with open(file_name, 'r') as file:
    updated_content = file.read()
    print(updated_content)
