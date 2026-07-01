# =======================================================
#       PYTHON STRING INDEXING & SLICING
# =======================================================

"""
Definition:
String indexing is used to access individual characters
of a string using their position (index).

Every character in a string has a unique index.

Python supports:
1. Positive Indexing
2. Negative Indexing
"""

# =======================================================
# 1. WHAT IS STRING INDEXING?
# =======================================================

"""
Definition:
String indexing is used to access a specific character
from a string using its index number.

Python indexing starts from 0.

Syntax:
string[index]

Example:
"""

text = "Python"

print("String:", text)
print(type(text))


# =======================================================
# 2. WHY DO WE USE INDEXING?
# =======================================================

"""
Definition:
Indexing allows us to access a single character
from a string without printing the whole string.

Example:
"""

language = "Python"

print("\nFirst Character:", language[0])
print("Second Character:", language[1])
print("Third Character:", language[2])


# =======================================================
# 3. POSITIVE INDEXING
# =======================================================

"""
Definition:
Positive indexing starts from the left side.

The first character always has index 0.

Example:

P   y   t   h   o   n
0   1   2   3   4   5
"""

word = "Python"

print("\nPositive Indexing")

print("Index 0 :", word[0])
print("Index 1 :", word[1])
print("Index 2 :", word[2])
print("Index 3 :", word[3])
print("Index 4 :", word[4])
print("Index 5 :", word[5])


# =======================================================
# 4. NEGATIVE INDEXING
# =======================================================

"""
Definition:
Negative indexing starts from the right side.

The last character always has index -1.

Example:

P   y   t   h   o   n
-6 -5 -4 -3 -2 -1
"""

word = "Python"

print("\nNegative Indexing")

print("Index -1 :", word[-1])
print("Index -2 :", word[-2])
print("Index -3 :", word[-3])
print("Index -4 :", word[-4])
print("Index -5 :", word[-5])
print("Index -6 :", word[-6])


# =======================================================
# 5. ACCESSING CHARACTERS
# =======================================================

"""
Definition:
Characters can be accessed using both
positive and negative indexes.

Example:
"""

name = "Programming"

print("\nAccessing Characters")

print("First Character :", name[0])
print("Fourth Character:", name[3])
print("Last Character  :", name[-1])
print("Second Last     :", name[-2])
# =======================================================
# 6. WHAT IS STRING SLICING?
# =======================================================

"""
Definition:
String slicing is used to extract a part of a string.

Instead of accessing one character, slicing returns
multiple characters.

Syntax:
string[start : end]

Note:
- The start index is included.
- The end index is excluded.

Example:
"""

text = "Python"

print("\nOriginal String:", text)
print(type(text))


# =======================================================
# 7. BASIC SLICING
# =======================================================

"""
Definition:
Basic slicing returns characters from the
starting index to the ending index.

Example:

P   y   t   h   o   n
0   1   2   3   4   5
"""

word = "Python"

print("\nBasic Slicing")

print("word[0:2] =", word[0:2])     # Py
print("word[0:4] =", word[0:4])     # Pyth
print("word[2:5] =", word[2:5])     # tho
print("word[1:6] =", word[1:6])     # ython


# =======================================================
# 8. START INDEX
# =======================================================

"""
Definition:
If only the start index is given,
Python starts from that position
and continues until the end of the string.

Syntax:
string[start:]

Example:
"""

language = "Programming"

print("\nStart Index")

print(language[0:])
print(language[3:])
print(language[5:])
print(language[7:])


# =======================================================
# 9. END INDEX
# =======================================================

"""
Definition:
If only the end index is given,
Python starts from index 0 and
stops before the given end index.

Syntax:
string[:end]

Example:
"""

language = "Programming"

print("\nEnd Index")

print(language[:3])
print(language[:5])
print(language[:7])
print(language[:10])


# =======================================================
# 10. STEP VALUE
# =======================================================

"""
Definition:
The step value tells Python how many
characters to skip while slicing.

Syntax:
string[start:end:step]

Example:
"""

text = "Programming"

print("\nStep Value")

print("text[::1] =", text[::1])      # Original String
print("text[::2] =", text[::2])      # Every second character
print("text[::3] =", text[::3])      # Every third character
print("text[1::2] =", text[1::2])    # Start from index 1


# =======================================================
# 11. REVERSE STRING
# =======================================================

"""
Definition:
A string can be reversed by using
a negative step value (-1).

Syntax:
string[::-1]

Example:
"""

text = "Python"

print("\nOriginal String :", text)
print("Reversed String :", text[::-1])


# Another Example

name = "Programming"

print("\nOriginal :", name)
print("Reversed :", name[::-1])
# =======================================================
# 12. COMMON ERRORS
# =======================================================

"""
Definition:
Beginners often make mistakes while using
string indexing and slicing.

Let's look at some common errors.
"""

text = "Python"

print("\nOriginal String:", text)

# -------------------------------------------------------
# Error 1: Index Out of Range
# -------------------------------------------------------

"""
Definition:
Trying to access an index that does not exist.

Example:
"""

# print(text[10])

"""
Output:
IndexError: string index out of range

Explanation:
The string "Python" has only 6 characters.
Valid indexes are:

0  1  2  3  4  5

Trying to access index 10 will produce an error.
"""


# -------------------------------------------------------
# Error 2: Using String Instead of Integer
# -------------------------------------------------------

"""
Definition:
Indexes must always be integers.

Example:
"""

# print(text["1"])

"""
Output:
TypeError: string indices must be integers

Explanation:
Python expects an integer index,
not a string.
"""


# -------------------------------------------------------
# Error 3: Forgetting the Colon in Slicing
# -------------------------------------------------------

"""
Wrong:
text[03]

Correct:
text[0:3]
"""

print("\nCorrect Slicing:", text[0:3])


# -------------------------------------------------------
# Error 4: Empty Slice
# -------------------------------------------------------

"""
If the start index is greater than
the end index, Python returns an empty string.
"""

print("\nEmpty Slice Example:")
print(text[5:2])


# =======================================================
# 13. PRACTICE EXAMPLES
# =======================================================

"""
Practice these examples to understand
indexing and slicing better.
"""

word = "Programming"

print("\nPractice Examples")

# First Character
print("First Character :", word[0])

# Last Character
print("Last Character :", word[-1])

# First Five Characters
print("First Five :", word[:5])

# Last Four Characters
print("Last Four :", word[-4:])

# Middle Characters
print("Middle :", word[3:8])

# Every Second Character
print("Every Second :", word[::2])

# Reverse String
print("Reverse :", word[::-1])


# =======================================================
# MINI EXERCISES
# =======================================================

"""
quiz 

1. Print the first character of "Computer"

2. Print the last character of "Python"

3. Print "Program" from "Programming"

4. Print "ming" from "Programming"

5. Reverse the word "Developer"

6. Print every second character of "Artificial"

7. Print every third character of "Programming"

8. Print the last five characters of "Technology"

9. Print the first six characters of "MachineLearning"

10. Reverse "Data Science"
"""
# =======================================================
# PRACTICE EXAMPLES WITH SOLUTIONS
# =======================================================

# 1. Print the first character of "Computer"

word = "Computer"
print("1.", word[0])


# 2. Print the last character of "Python"

word = "Python"
print("2.", word[-1])


# 3. Print "Program" from "Programming"

word = "Programming"
print("3.", word[:7])


# 4. Print "ming" from "Programming"

word = "Programming"
print("4.", word[-4:])


# 5. Reverse the word "Developer"

word = "Developer"
print("5.", word[::-1])


# 6. Print every second character of "Artificial"

word = "Artificial"
print("6.", word[::2])


# 7. Print every third character of "Programming"

word = "Programming"
print("7.", word[::3])


# 8. Print the last five characters of "Technology"

word = "Technology"
print("8.", word[-5:])


# 9. Print the first six characters of "MachineLearning"

word = "MachineLearning"
print("9.", word[:6])


# 10. Reverse "Data Science"

word = "Data Science"
print("10.", word[::-1])

# =======================================================
# SUMMARY
# =======================================================

"""
STRING INDEXING & SLICING SUMMARY

✔ Indexing is used to access individual characters.

✔ Python supports:
   • Positive Indexing
   • Negative Indexing

✔ Positive Indexing starts from 0.

✔ Negative Indexing starts from -1.

✔ Slicing is used to extract a part of a string.

✔ Syntax:
   string[start:end]

✔ Step Value:
   string[start:end:step]

✔ Reverse String:
   string[::-1]

✔ Common Errors:
   • IndexError
   • TypeError

✔ Indexing and slicing make working
  with strings easy and efficient.
"""