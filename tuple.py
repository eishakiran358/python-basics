# ==========================================================
# 1. What is a Tuple?
# ==========================================================

"""
Definition:
A Tuple is an ordered and immutable
collection in Python. Once created,
its elements cannot be changed.
"""

# ==========================================================
# 2. Why Use Tuples?
# ==========================================================

"""
Advantages of Tuples

1. Ordered
2. Immutable (Cannot be Changed)
3. Allow Duplicate Values
4. Faster than Lists
5. Can Store Different Data Types
"""

# ==========================================================
# 3. Creating a Tuple
# ==========================================================

print("========== Creating a Tuple ==========")

fruits = ("Apple", "Banana", "Mango")

print(fruits)

print()

# ==========================================================
# 4. Tuple Data Types
# ==========================================================

print("========== Tuple Data Types ==========")

mixed = (10, 20.5, "Python", True)

print(mixed)

print()

# ==========================================================
# 5. Access Tuple Items
# ==========================================================

print("========== Access Tuple Items ==========")

fruits = ("Apple", "Banana", "Mango", "Orange")

print("First Item :", fruits[0])
print("Third Item :", fruits[2])

print()

# ==========================================================
# 6. Positive Indexing
# ==========================================================

print("========== Positive Indexing ==========")

numbers = (10, 20, 30, 40, 50)

print(numbers[0])
print(numbers[1])
print(numbers[4])

print()

# ==========================================================
# 7. Negative Indexing
# ==========================================================

print("========== Negative Indexing ==========")

numbers = (10, 20, 30, 40, 50)

print(numbers[-1])
print(numbers[-2])

print()

# ==========================================================
# 8. Tuple Slicing
# ==========================================================

print("========== Tuple Slicing ==========")

numbers = (10, 20, 30, 40, 50, 60)

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])

print()

# ==========================================================
# 9. Tuple Length
# ==========================================================

print("========== Tuple Length ==========")

numbers = (10, 20, 30, 40, 50)

print("Length =", len(numbers))

print()

# ==========================================================
# 10. Check Item Exists
# ==========================================================

print("========== Check Item Exists ==========")

fruits = ("Apple", "Banana", "Mango")

if "Banana" in fruits:
    print("Banana Found")
else:
    print("Banana Not Found")

print()

# ==========================================================
# 11. Loop Through a Tuple
# ==========================================================

print("========== Loop Through a Tuple ==========")

fruits = ("Apple", "Banana", "Mango")

for fruit in fruits:
    print(fruit)

print()

# ==========================================================
# 12. Nested Tuples
# ==========================================================

print("========== Nested Tuples ==========")

students = (
    ("Ali", 20),
    ("Ahmed", 22),
    ("Sara", 19)
)

print(students)
print("First Student :", students[0])
print("Student Name  :", students[1][0])

print()

# ==========================================================
# 13. Tuple Packing
# ==========================================================

print("========== Tuple Packing ==========")

student = ("Ali", 20, "Python")

print(student)

print()

# ==========================================================
# 14. Tuple Unpacking
# ==========================================================

print("========== Tuple Unpacking ==========")

name, age, course = ("Ali", 20, "Python")

print("Name   :", name)
print("Age    :", age)
print("Course :", course)

print()

# ==========================================================
# 15. Join Tuples
# ==========================================================

print("========== Join Tuples ==========")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

tuple3 = tuple1 + tuple2

print(tuple3)

print()

# ==========================================================
# 16. Tuple Methods
# ==========================================================

print("========== Tuple Methods ==========")

numbers = (10, 20, 10, 30, 40, 10)

print("count(10) =", numbers.count(10))
print("index(30) =", numbers.index(30))

print()

# ==========================================================
# 17. Delete a Tuple
# ==========================================================

print("========== Delete a Tuple ==========")

colors = ("Red", "Green", "Blue")

print("Before Delete :", colors)

del colors

print("Tuple Deleted Successfully")

print()

# ==========================================================
# 18. Difference Between List and Tuple
# ==========================================================

print("========== List vs Tuple ==========")

print("List  : Mutable (Can be Changed)")
print("Tuple : Immutable (Cannot be Changed)")

print()

# ==========================================================
# 19. Sum of Tuple
# ==========================================================

print("========== Sum of Tuple ==========")

"""
Definition:
Calculate the sum of all
elements in a tuple.
"""

numbers = (10, 20, 30, 40, 50)

total = sum(numbers)

print("Tuple :", numbers)
print("Sum   :", total)

print()


# ==========================================================
# 20. Largest Number
# ==========================================================

print("========== Largest Number ==========")

"""
Definition:
Find the largest number
from a tuple.
"""

numbers = (45, 12, 89, 23, 67)

print("Tuple           :", numbers)
print("Largest Number  :", max(numbers))

print()


# ==========================================================
# 21. Smallest Number
# ==========================================================

print("========== Smallest Number ==========")

"""
Definition:
Find the smallest number
from a tuple.
"""

numbers = (45, 12, 89, 23, 67)

print("Tuple            :", numbers)
print("Smallest Number  :", min(numbers))

print()


# ==========================================================
# 22. Find Even Numbers
# ==========================================================

print("========== Find Even Numbers ==========")

"""
Definition:
Print all even numbers
from a tuple.
"""

numbers = (10, 15, 20, 25, 30, 35, 40)

print("Even Numbers:")

for number in numbers:

    if number % 2 == 0:
        print(number)

print()


# ==========================================================
# 23. Find Odd Numbers
# ==========================================================

print("========== Find Odd Numbers ==========")

"""
Definition:
Print all odd numbers
from a tuple.
"""

numbers = (10, 15, 20, 25, 30, 35, 40)

print("Odd Numbers:")

for number in numbers:

    if number % 2 != 0:
        print(number)

print()


# ==========================================================
# 24. Count Positive & Negative Numbers
# ==========================================================

print("========== Count Positive & Negative ==========")

"""
Definition:
Count positive and negative
numbers in a tuple.
"""

numbers = (10, -5, 30, -20, 15, -1, 0)

positive = 0
negative = 0

for number in numbers:

    if number > 0:
        positive += 1

    elif number < 0:
        negative += 1

print("Positive Numbers :", positive)
print("Negative Numbers :", negative)

print()


# ==========================================================
# 25. Search an Element
# ==========================================================

print("========== Search an Element ==========")

"""
Definition:
Search an element
inside a tuple.
"""

numbers = (5, 10, 15, 20, 25)

search = int(input("Enter Number to Search: "))

if search in numbers:
    print(search, "Found in Tuple")

else:
    print(search, "Not Found")

print()


# ==========================================================
# 26. Reverse a Tuple
# ==========================================================

print("========== Reverse a Tuple ==========")

"""
Definition:
Reverse a tuple using slicing.
"""

numbers = (10, 20, 30, 40, 50)

reverse_tuple = numbers[::-1]

print("Original Tuple :", numbers)
print("Reversed Tuple :", reverse_tuple)

print()


# ==========================================================
# 27. Remove Duplicates
# ==========================================================

print("========== Remove Duplicates ==========")

"""
Definition:
Remove duplicate values
from a tuple.
"""

numbers = (10, 20, 10, 30, 40, 20, 50)

unique_tuple = tuple(set(numbers))

print("Original Tuple :", numbers)
print("Unique Tuple   :", unique_tuple)

print()


# ==========================================================
# 28. Second Largest Number
# ==========================================================

print("========== Second Largest Number ==========")

"""
Definition:
Find the second largest
number in a tuple.
"""

numbers = (10, 50, 20, 80, 40, 60)

sorted_numbers = sorted(numbers)

print("Tuple           :", numbers)
print("Second Largest  :", sorted_numbers[-2])

print()


# ==========================================================
# 29. Find Maximum & Minimum
# ==========================================================

print("========== Maximum & Minimum ==========")

"""
Definition:
Find the maximum and minimum
values in a tuple.
"""

numbers = (25, 15, 80, 10, 45)

print("Maximum :", max(numbers))
print("Minimum :", min(numbers))

print()


# ==========================================================
# 30. Average of Tuple
# ==========================================================

print("========== Average of Tuple ==========")

"""
Definition:
Calculate the average
of tuple elements.
"""

numbers = (10, 20, 30, 40, 50)

average = sum(numbers) / len(numbers)

print("Tuple   :", numbers)
print("Average :", average)

print()


# ==========================================================
# 31. Student Marks Record
# ==========================================================

print("========== Student Marks Record ==========")

"""
Definition:
Store student marks in a tuple and calculate
the total, average, highest, and lowest marks.
"""

marks = []

for i in range(5):
    mark = float(input(f"Enter Marks of Subject {i + 1}: "))
    marks.append(mark)

marks = tuple(marks)

print("\nStudent Marks :", marks)
print("Total Marks   :", sum(marks))
print("Average Marks :", sum(marks) / len(marks))
print("Highest Marks :", max(marks))
print("Lowest Marks  :", min(marks))

print()


# ==========================================================
# 32. Employee Information System
# ==========================================================

print("========== Employee Information System ==========")

"""
Definition:
Store employee information using tuples.
"""

employee = (
    input("Enter Employee ID: "),
    input("Enter Employee Name: "),
    input("Enter Department: "),
    float(input("Enter Salary: "))
)

print("\n===== Employee Details =====")
print("ID         :", employee[0])
print("Name       :", employee[1])
print("Department :", employee[2])
print("Salary     :", employee[3])

print()


# ==========================================================
# 33. Product Details System
# ==========================================================

print("========== Product Details System ==========")

"""
Definition:
Store product information in a tuple.
"""

product = (
    input("Enter Product ID: "),
    input("Enter Product Name: "),
    float(input("Enter Product Price: "))
)

print("\n===== Product Details =====")
print("Product ID    :", product[0])
print("Product Name  :", product[1])
print("Product Price :", product[2])

print()


# ==========================================================
# 34. Student Attendance Record
# ==========================================================

print("========== Student Attendance Record ==========")

"""
Definition:
Store attendance status of students
using tuples.
"""

attendance = (
    ("Ali", "Present"),
    ("Ahmed", "Absent"),
    ("Sara", "Present"),
    ("Ayesha", "Present")
)

print("\nAttendance Record")

for student in attendance:

    print("----------------------")
    print("Name   :", student[0])
    print("Status :", student[1])

print()