"""
Definition:
A data type specifies the type of value a variable can store.

Example:
name = "Eishaa"   # String
age = 21          # Integer
"""


"""
Python Data Types:

Text Type:
    str

Numeric Types:
    int, float, complex

Sequence Types:
    list, tuple

Mapping Type:
    dict

Set Types:
    set

Boolean Type:
    bool

None Type:
    NoneType
"""

#..          .............. str (String)................
"""
Definition:
String is used to store text or characters.

Example:
"""
message = "Hello World"
print("String:", message)
print(type(message))

#............................... int (Integer)......................
"""
Definition:
Integer is used to store whole numbers without decimal points.

Example:
"""
age = 20
print("\nInteger:", age)
print(type(age))


# ...................................float
"""
Definition:
Float is used to store decimal numbers.

Example:
"""
price = 20.5
print("\nFloat:", price)
print(type(price))

# .........................complex
"""
Definition:
Complex is used to store complex numbers.
Example:
"""
number = 1 + 2j

print("\nComplex:", number)
print(type(number))

#....................... list.........................
"""
Definition:
A list is an ordered and changeable collection.
Lists allow duplicate values.
Example:
"""
fruits = ["apple", "banana", "cherry"]
print("\nList:", fruits)
print(type(fruits))

#....................... tuple.........................
"""
Definition:
A tuple is an ordered and unchangeable collection.
Tuples allow duplicate values.

Example:
"""
colors = ("red", "green", "blue")
print("\nTuple:", colors)
print(type(colors))

#..................... dict (Dictionary)..........................
"""
Definition:
Dictionary stores data in key-value pairs.

Example:
"""
student = {
    "name": "John",
    "age": 25
}
print("\nDictionary:", student)
print(type(student))

#.............................. set.................................
"""
Definition:
A set is an unordered collection of unique values.

Example:
"""

fruits_set = {"apple", "banana", "cherry"}

print("\nSet:", fruits_set)
print(type(fruits_set))
#............................. bool.................................
"""
Definition:
Boolean data type represents only two values:
True or False.

Example:
"""
is_student = True
print("\nBoolean:", is_student)
print(type(is_student))

#............................... NoneType..............................
"""
Definition:
NoneType represents no value or an empty value.

Example:
"""
value = None
print("\nNone:", value)
print(type(value))


# =======================================================
#                 PYTHON type() FUNCTION
# =======================================================

"""
Definition:
The type() function is used to find the data type of a variable or value.

Syntax:
type(object)

Return:
It returns the data type (class) of the given object.

# ========================================
#         type() Function
#========================================

Purpose:
    Finds the data type of a variable or value.
Syntax:
    type(object)
Examples:
    type("Hello")      -> <class 'str'>
    type(100)          -> <class 'int'>
    type(10.5)         -> <class 'float'>
    type([1, 2, 3])    -> <class 'list'>
    type(True)         -> <class 'bool'>
"""

# =======================================================
# Example 1: String
# =======================================================

name = "Eishaa"

print("Value :", name)
print("Data Type :", type(name))


# =======================================================
# Example 2: Integer
# =======================================================

age = 21

print("\nValue :", age)
print("Data Type :", type(age))


# =======================================================
# Example 3: Float
# =======================================================

price = 99.99

print("\nValue :", price)
print("Data Type :", type(price))


# =======================================================
# Example 4: Complex
# =======================================================

number = 5 + 3j

print("\nValue :", number)
print("Data Type :", type(number))


# =======================================================
# Example 5: List
# =======================================================

fruits = ["Apple", "Banana", "Cherry"]

print("\nValue :", fruits)
print("Data Type :", type(fruits))


# =======================================================
# Example 6: Tuple
# =======================================================

colors = ("Red", "Green", "Blue")

print("\nValue :", colors)
print("Data Type :", type(colors))


# =======================================================
# Example 7: Dictionary
# =======================================================

student = {
    "Name": "Ali",
    "Age": 20
}

print("\nValue :", student)
print("Data Type :", type(student))


# =======================================================
# Example 8: Set
# =======================================================

numbers = {1, 2, 3, 4}

print("\nValue :", numbers)
print("Data Type :", type(numbers))


# =======================================================
# Example 9: Boolean
# =======================================================

is_student = True

print("\nValue :", is_student)
print("Data Type :", type(is_student))
# =======================================================
# Example 10: NoneType
# =======================================================

value = None

print("\nValue :", value)
print("Data Type :", type(value))
