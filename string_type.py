"""
===========================================
        PYTHON STRINGS
===========================================

Definition:
A string is a sequence of characters enclosed
inside quotation marks.

A string can contain:
• Letters
• Numbers
• Symbols
• Spaces

Data Type:
str
"""
name = "Eishaa"

print(name)
print(type(name))
"""
================================================
2. Creating Strings
===============================================
A. Single Quotes
city = 'Karachi'
print(city)


B. Double Quotes
country = "Pakistan"

print(country)

C. Triple Quotes

Used for paragraphs or multiple lines."""

paragraph =""" Python is easy.
Python is powerful.
Python is fun

print(paragraph)"""

print(paragraph)

# =====================================
# 3. Single vs Double Quotes
======================================
# Both are exactly the same.

a = 'Hello'
b = "Hello"
print(a)
print(b)

#=======================================================
#ESCAPE CHARACTERS
#=======================================================
'''........................What are Escape Characters?...............................
Definition

Escape characters are special characters that start with a backslash (\).

They are used to perform special actions inside a string.

For example:

Move text to the next line
Add a tab (space)
Print quotation marks
Print a backslash
Why do we use Escape Characters?

Sometimes we want to print something that Python normally treats as special.

For example:'''

print("I'm learning Python")

# This works because the apostrophe (') is inside double quotes.

# But this does not work:

#print('I'm learning Python')

# Python thinks the string ends after I.
# So we use an escape character.

print('I\'m learning Python')


# The backslash (\) tells Python:

"The next character is part of the string."

#================================
# Common Escape Characters
#================================
'''1.
Definition

Used to print a single quote inside a string.

Example'''

print('I\'m learning Python')


# Without \

# print('I'm learning Python')

# Output

# SyntaxError
'''2. "
Definition

Used to print a double quote inside a string.

Example'''

print("He said \"Hello\"")

'''
3 \
Definition

Used to print a backslash.

Because one backslash starts an escape sequence.

Example'''

print("C:\\Users\\Ali")
# Output
# C:\Users\Ali

# Real Example
# Windows Path
# C:\Program Files\Python
# path = "C:\\Program Files\\Python"
# print(path)

'''4. \n
Definition

Moves the text to a new line.

Example'''

print("Hello\nWorld")
print("Python\nJava\nC++")

# ==========================================================
#            PYTHON STRING INDEXING AND SLICING
# ==========================================================

"""
File Name : 05_String_Indexing_and_Slicing.py

Topics Covered
--------------
1. What is Indexing?
2. Positive Indexing
3. Negative Indexing
4. Accessing Characters
5. What is Slicing?
6. Basic Slicing
7. Start Index
8. End Index
9. Step Value
10. Reverse String
11. Common Errors
12. Practice Examples
13. Summary
"""

# ==========================================================
# 1. What is Indexing?
# ==========================================================

"""
Definition:
-----------
Indexing is used to access a single character from a string.

Every character in a string has its own position number,
called an index.

Python provides two types of indexing:

1. Positive Indexing
2. Negative Indexing
"""

text = "Python"

print(text)

# ==========================================================
# 2. Positive Indexing
# ==========================================================

"""
Positive indexing starts from LEFT to RIGHT.

The first character always starts with index 0.

Example:

P   y   t   h   o   n
0   1   2   3   4   5
"""

word = "Python"

print("First Character :", word[0])   # P
print("Second Character:", word[1])   # y
print("Third Character :", word[2])   # t
print("Fourth Character:", word[3])   # h
print("Fifth Character :", word[4])   # o
print("Sixth Character :", word[5])   # n


# ==========================================================
# 3. Negative Indexing
# ==========================================================

"""
Negative indexing starts from RIGHT to LEFT.

The last character always starts with index -1.

Example:

 P   y   t   h   o   n
-6 -5  -4  -3  -2  -1
"""

word = "Python"

print("Last Character      :", word[-1])   # n
print("Second Last         :", word[-2])   # o
print("Third Last          :", word[-3])   # h
print("Fourth Last         :", word[-4])   # t
print("Fifth Last          :", word[-5])   # y
print("First Character     :", word[-6])   # P


# ==========================================================
# 4. Accessing Characters
# ==========================================================

"""
Use square brackets [] with an index number
to access a character.
"""

language = "Programming"

print(language[0])     # P
print(language[4])     # r
print(language[-1])    # g
print(language[-5])    # m


# ==========================================================
# 5. What is Slicing?
# ==========================================================

"""
Definition:
-----------
Slicing is used to extract multiple characters
from a string.

Syntax:

string[start:end]

The end index is NOT included.
"""

text = "Python Programming"

print(text[0:6])     # Python


# ==========================================================
# 6. Basic Slicing
# ==========================================================

word = "Programming"

print(word[0:4])      # Prog
print(word[4:7])      # ram
print(word[3:9])      # gramm
print(word[:5])       # Progr
print(word[5:])       # amming
print(word[:])        # Complete String


# ==========================================================
# 7. Start Index
# ==========================================================

"""
The start index tells Python
where to begin slicing.
"""

text = "Artificial Intelligence"

print(text[0:10])      # Artificial
print(text[11:23])     # Intelligence


# ==========================================================
# 8. End Index
# ==========================================================

"""
The end index tells Python
where to stop slicing.

Remember:
The end index is NOT included.
"""

word = "Computer"

print(word[0:4])    # Comp
print(word[4:8])    # uter


# ==========================================================
# 9. Step Value
# ==========================================================

"""
Syntax:

string[start:end:step]

Step tells Python how many characters
to skip.
"""

text = "ABCDEFGHIJK"

print(text[::1])      # ABCDEFGHIJK
print(text[::2])      # ACEGIK
print(text[::3])      # ADGJ
print(text[1::2])     # BDFHJ


# ==========================================================
# 10. Reverse String
# ==========================================================

"""
Use a negative step (-1)
to reverse a string.
"""

word = "Python"

print(word[::-1])     # nohtyP

name = "ChatGPT"

print(name[::-1])


# ==========================================================
# 11. Common Errors
# ==========================================================

"""
1. IndexError
---------------
Occurs when the index does not exist.
"""

word = "Python"

# print(word[10])
# IndexError


"""
2. TypeError
-------------
Index must be an integer.
"""

# print(word["1"])
# TypeError


"""
3. Remember:
-------------
Strings are Immutable.

Characters cannot be changed directly.
"""

text = "Python"

# text[0] = "J"
# TypeError

print(text)


# ==========================================================
# 12. Practice Examples
# ==========================================================

name = "Artificial Intelligence"

print("First Character      :", name[0])
print("Last Character       :", name[-1])

print("First 10 Characters  :", name[:10])

print("Last 12 Characters   :", name[-12:])

print("Every 2nd Character  :", name[::2])

print("Reverse String       :", name[::-1])

print("Middle Characters    :", name[5:15])


# ==========================================================
# More Practice
# ==========================================================

course = "Python Programming"

print(course[0])
print(course[-1])

print(course[:6])

print(course[7:18])

print(course[::-1])

print(course[::2])


# ==========================================================
# Mini Challenge
# ==========================================================

"""

String = "Machine Learning"

1. Print first character.
2. Print last character.
3. Print "Machine".
4. Print "Learning".
5. Print complete string.
6. Print every second character.
7. Reverse the string.
"""

sample = "Machine Learning"

print(sample[0])

print(sample[-1])

print(sample[:7])

print(sample[8:])

print(sample[:])

print(sample[::2])

print(sample[::-1])


# ==========================================================
# 13. Summary
# ==========================================================

"""
✓ Indexing is used to access one character.

✓ Positive indexing starts from 0.

✓ Negative indexing starts from -1.

✓ Slicing extracts multiple characters.

✓ Syntax:
    string[start:end]

✓ End index is NOT included.

✓ Step value skips characters.

✓ [::-1] reverses a string.

✓ Strings are immutable (cannot be changed directly).
"""

print("\n===== END OF STRING INDEXING AND SLICING =====")


# ==========================================================
#               PYTHON STRING METHODS
# ==========================================================

"""
Topics Covered
--------------
1. upper()
2. lower()
3. title()
4. capitalize()
5. strip()
6. replace()
7. split()
8. join()
9. find()
10. index()
11. count()
12. startswith()
13. endswith()
14. isalpha()
15. isdigit()
16. isalnum()
17. isspace()
18. swapcase()
19. casefold()
20. Summary
"""

# ==========================================================
# 1. upper()
# ==========================================================

"""
Definition:
-----------
The upper() method converts all letters
of a string into UPPERCASE.
"""

text = "python programming"

print(text.upper())
# Output: PYTHON PROGRAMMING


# ==========================================================
# 2. lower()
# ==========================================================

"""
Definition:
-----------
The lower() method converts all letters
into lowercase.
"""

text = "PYTHON PROGRAMMING"

print(text.lower())
# Output: python programming


# ==========================================================
# 3. title()
# ==========================================================

"""
Definition:
-----------
The title() method converts the first letter
of every word into uppercase.
"""

text = "python programming language"

print(text.title())
# Output: Python Programming Language


# ==========================================================
# 4. capitalize()
# ==========================================================

"""
Definition:
-----------
The capitalize() method converts only
the first letter of the string into uppercase.
"""

text = "python programming"

print(text.capitalize())
# Output: Python programming


# ==========================================================
# 5. strip()
# ==========================================================

"""
Definition:
-----------
The strip() method removes extra spaces
from the beginning and the end of a string.
"""

text = "   Python Programming   "

print(text.strip())
# Output: Python Programming


# ==========================================================
# 6. replace()
# ==========================================================

"""
Definition:
-----------
The replace() method replaces one word
or character with another.
"""

text = "I like Java"

print(text.replace("Java", "Python"))
# Output: I like Python


# ==========================================================
# 7. split()
# ==========================================================

"""
Definition:
-----------
The split() method converts a string
into a list.
"""

text = "Python Java C++ JavaScript"

print(text.split())
# Output: ['Python', 'Java', 'C++', 'JavaScript']


# ==========================================================
# 8. join()
# ==========================================================

"""
Definition:
-----------
The join() method joins list items
into a single string.
"""

languages = ["Python", "Java", "C++"]

print(" - ".join(languages))
# Output: Python - Java - C++


# ==========================================================
# 9. find()
# ==========================================================

"""
Definition:
-----------
The find() method returns the first
index of a character or word.

If not found, it returns -1.
"""

text = "Python Programming"

print(text.find("P"))
print(text.find("Programming"))
print(text.find("Java"))


# ==========================================================
# 10. index()
# ==========================================================

"""
Definition:
-----------
The index() method returns the position
of a character or word.

If not found, it gives an error.
"""

text = "Python Programming"

print(text.index("P"))
print(text.index("Programming"))

# print(text.index("Java"))
# ValueError


# ==========================================================
# 11. count()
# ==========================================================

"""
Definition:
-----------
The count() method counts how many times
a character or word appears.
"""

text = "Python Python Java Python"

print(text.count("Python"))
print(text.count("Java"))


# ==========================================================
# 12. startswith()
# ==========================================================

"""
Definition:
-----------
The startswith() method checks whether
a string starts with a specific value.

Returns:
True or False
"""

text = "Python Programming"

print(text.startswith("Python"))
print(text.startswith("Java"))


# ==========================================================
# 13. endswith()
# ==========================================================

"""
Definition:
-----------
The endswith() method checks whether
a string ends with a specific value.

Returns:
True or False
"""

text = "Python Programming"

print(text.endswith("Programming"))
print(text.endswith("Python"))


# ==========================================================
# 14. isalpha()
# ==========================================================

"""
Definition:
-----------
Returns True if all characters
are alphabets.
"""

print("Python".isalpha())
print("Python123".isalpha())


# ==========================================================
# 15. isdigit()
# ==========================================================

"""
Definition:
-----------
Returns True if all characters
are digits.
"""

print("12345".isdigit())
print("123ABC".isdigit())


# ==========================================================
# 16. isalnum()
# ==========================================================

"""
Definition:
-----------
Returns True if the string contains
only letters and numbers.
"""

print("Python123".isalnum())
print("Python 123".isalnum())


# ==========================================================
# 17. isspace()
# ==========================================================

"""
Definition:
-----------
Returns True if the string
contains only spaces.
"""

print("     ".isspace())
print("Python".isspace())


# ==========================================================
# 18. swapcase()
# ==========================================================

"""
Definition:
-----------
The swapcase() method changes
uppercase letters into lowercase
and lowercase letters into uppercase.
"""

text = "Python Programming"

print(text.swapcase())
# Output: pYTHON pROGRAMMING


# ==========================================================
# 19. casefold()
# ==========================================================

"""
Definition:
-----------
The casefold() method converts
a string into lowercase.

It is stronger than lower()
and is mainly used for
case-insensitive comparisons.
"""

text = "PYTHON"

print(text.casefold())
# Output: python


# ==========================================================
# Practice Examples
# ==========================================================

sentence = "   Artificial Intelligence with Python   "

print(sentence.upper())

print(sentence.lower())

print(sentence.title())

print(sentence.strip())

print(sentence.replace("Python", "Machine Learning"))

print(sentence.split())

print(sentence.find("Python"))

print(sentence.count("i"))

print(sentence.startswith(" "))

print(sentence.endswith(" "))


# ==========================================================
# Mini Challenge
# ==========================================================

"""
Try Yourself

String = "Python Programming"

1. Convert into uppercase.
2. Convert into lowercase.
3. Convert into title case.
4. Replace "Programming" with "Developer".
5. Count letter 'P'.
6. Check whether it starts with "Python".
7. Check whether it ends with "Developer".
8. Split the string.
"""

text = "Python Programming"

print(text.upper())

print(text.lower())

print(text.title())

print(text.replace("Programming", "Developer"))

print(text.count("P"))

print(text.startswith("Python"))

print(text.endswith("Developer"))

print(text.split())


# ==========================================================
# 20. Summary
# ==========================================================

"""
✓ upper()      → Converts all letters to uppercase.

✓ lower()      → Converts all letters to lowercase.

✓ title()      → Capitalizes every word.

✓ capitalize() → Capitalizes only the first letter.

✓ strip()      → Removes extra spaces.

✓ replace()    → Replaces text.

✓ split()      → Converts a string into a list.

✓ join()       → Joins list items into one string.

✓ find()       → Returns index or -1 if not found.

✓ index()      → Returns index or raises an error.

✓ count()      → Counts occurrences.

✓ startswith() → Checks starting text.

✓ endswith()   → Checks ending text.

✓ isalpha()    → Checks only letters.

✓ isdigit()    → Checks only digits.

✓ isalnum()    → Checks letters and numbers.

✓ isspace()    → Checks only spaces.

✓ swapcase()   → Swaps uppercase and lowercase.

✓ casefold()   → Strong lowercase conversion.
"""

print("\n===== END OF STRING METHODS =====")

# ==========================================================
# 1. What is String Formatting?
# ==========================================================

"""
Definition:
-----------
String Formatting is used to insert values
inside a string in a clean and readable way.

Python provides different ways
to format strings:

1. Concatenation (+)
2. format() Method
3. f-Strings
"""

name = "Alice"
age = 22

print("Name:", name)
print("Age :", age)


# ==========================================================
# 2. Concatenation (+)
# ==========================================================

"""
Definition:
-----------
Concatenation means joining two or more
strings using the (+) operator.
"""

first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name

print(full_name)

# Joining words
print("Python" + " " + "Programming")

# Numbers must be converted into strings
age = 20

print("Age: " + str(age))


# ==========================================================
# 3. String Repetition (*)
# ==========================================================

"""
Definition:
-----------
The (*) operator repeats
a string multiple times.
"""

print("Python " * 3)

print("*" * 30)

print("Hello\n" * 5)
