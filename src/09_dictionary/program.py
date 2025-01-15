# Chapter 09: Dictionaries

"""
Introduction:
Dictionaries are powerful and versatile data structures in Python used to store key-value pairs. 
Each key in a dictionary must be unique and immutable, while the values can be of any data type and can repeat.

Key Concepts:
1. Dictionary Creation: Using curly braces `{}` to define key-value pairs.
2. Accessing and Modifying Data: Using keys to retrieve or update values.
3. Iterating Over Dictionaries: Using loops to process keys, values, or both.
4. Common Dictionary Methods: `.get()`, `.keys()`, `.values()`, `.items()`, `.update()`, etc.

Notes:
- Keys in a dictionary must be unique and hashable (e.g., strings, numbers, tuples).
- Values can be any data type and do not need to be unique.
- Dictionaries are unordered in Python versions < 3.7 but preserve order in Python 3.7+.

"""

# Program to Count the Occurrences of Words in a Sentence

# Input: Accept a sentence from the user
sentence = input("Enter a sentence: ").lower()

# Split the sentence into words
words = sentence.split()

# Create an empty dictionary to store word counts
word_count = {}

# Count occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display the word count dictionary
print("\nWord Counts:")
for word, count in word_count.items():
    print(f"{word}: {count}")

# Demonstrating Dictionary Methods
print("\nDictionary Methods in Action:")

# Access a value using .get()
search_word = input("\nEnter a word to search its count: ").lower()
count = word_count.get(search_word, 0)  # Returns 0 if the word is not found
print(f"The word '{search_word}' appears {count} times.")

# Display all keys
print("\nAll Words (Keys):", list(word_count.keys()))

# Display all values
print("Word Counts (Values):", list(word_count.values()))

# Add a new key-value pair
word_count["example"] = 1
print("\nAfter Adding a New Word:", word_count)

# Remove a key-value pair
word_count.pop("example", None)  # Removes 'example' if it exists
print("After Removing 'example':", word_count)
