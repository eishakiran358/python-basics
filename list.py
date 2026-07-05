
# ==========================================================
# Python Lists
# ==========================================================

print("========== Python Lists ==========\n")

# ==========================================================
# 1. What is a List?
# ==========================================================

"""
Definition:
A List is an ordered, mutable (changeable)
collection in Python. It can store multiple
values of different data types.
"""

# ==========================================================
# 2. Why Use Lists?
# ==========================================================

"""
Advantages of Lists

1. Store multiple values
2. Mutable (can be modified)
3. Ordered
4. Allow duplicate values
5. Can store different data types
"""

# ==========================================================
# 3. Creating a List
# ==========================================================

print("========== Creating a List ==========")

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits)

print()

# ==========================================================
# 4. List Data Types
# ==========================================================

print("========== List Data Types ==========")

mixed = [10, 20.5, "Python", True]

print(mixed)

print()

# ==========================================================
# 5. Access List Items
# ==========================================================

print("========== Access List Items ==========")

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("First Item :", fruits[0])
print("Third Item :", fruits[2])

print()

# ==========================================================
# 6. Positive Indexing
# ==========================================================

print("========== Positive Indexing ==========")

numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[1])
print(numbers[4])

print()

# ==========================================================
# 7. Negative Indexing
# ==========================================================

print("========== Negative Indexing ==========")

numbers = [10, 20, 30, 40, 50]

print(numbers[-1])
print(numbers[-2])

print()

# ==========================================================
# 8. List Slicing
# ==========================================================

print("========== List Slicing ==========")

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])

print()

# ==========================================================
# 9. Change List Items
# ==========================================================

print("========== Change List Items ==========")

fruits = ["Apple", "Banana", "Mango"]

print("Before :", fruits)

fruits[1] = "Orange"

print("After  :", fruits)

print()

# ==========================================================
# 10. Add Items
# ==========================================================

print("========== append() ==========")

fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)

print()

print("========== insert() ==========")

fruits.insert(1, "Orange")

print(fruits)

print()

print("========== extend() ==========")

fruits.extend(["Grapes", "Kiwi"])

print(fruits)

print()

# ==========================================================
# 11. Remove Items
# ==========================================================

print("========== remove() ==========")

numbers = [10, 20, 30, 40]

numbers.remove(20)

print(numbers)

print()

print("========== pop() ==========")

numbers.pop()

print(numbers)

print()

print("========== del ==========")

numbers = [10, 20, 30, 40]

del numbers[1]

print(numbers)

print()

print("========== clear() ==========")

numbers.clear()

print(numbers)

print()

# ==========================================================
# 12. Check Item Exists
# ==========================================================

print("========== Check Item Exists ==========")

fruits = ["Apple", "Banana", "Mango"]

if "Banana" in fruits:
    print("Banana Found")

else:
    print("Banana Not Found")

print()

# ==========================================================
# 13. List Length
# ==========================================================

print("========== List Length ==========")

numbers = [10, 20, 30, 40, 50]

print("Length =", len(numbers))

print()

# ==========================================================
# 14. Loop Through a List
# ==========================================================

print("========== Loop Through a List ==========")

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

print()

# ==========================================================
# 15. Nested Lists
# ==========================================================

print("========== Nested Lists ==========")

students = [
    ["Ali", 20],
    ["Ahmed", 22],
    ["Sara", 19]
]

print(students)

print("First Student :", students[0])
print("Student Name  :", students[1][0])

print()

# ==========================================================
# 16. Copy a List
# ==========================================================

print("========== Copy a List ==========")

list1 = [1, 2, 3]

list2 = list1.copy()

print("Original :", list1)
print("Copy     :", list2)

print()

# ==========================================================
# 17. Join Lists
# ==========================================================

print("========== Join Lists ==========")

list1 = [1, 2, 3]

list2 = [4, 5, 6]

list3 = list1 + list2

print(list3)

print()

# ==========================================================
# 18. List Methods
# ==========================================================

print("========== List Methods ==========")

numbers = [5, 3, 1, 4, 2]

numbers.sort()
print("sort()   :", numbers)

numbers.reverse()
print("reverse():", numbers)

numbers.append(10)
print("append() :", numbers)

numbers.insert(0, 100)
print("insert() :", numbers)

numbers.pop()
print("pop()    :", numbers)

print()

# ==========================================================
# 19. Sum of List
# ==========================================================

print("========== Sum of List ==========")

"""
Definition:
This program calculates the sum of all
elements in a list.
"""

numbers = [10, 20, 30, 40, 50]

total = sum(numbers)

print("List :", numbers)
print("Sum  :", total)

print()


# ==========================================================
# 20. Largest Number
# ==========================================================

print("========== Largest Number ==========")

"""
Definition:
This program finds the largest
number in a list.
"""

numbers = [45, 12, 89, 23, 67]

largest = max(numbers)

print("List            :", numbers)
print("Largest Number  :", largest)

print()


# ==========================================================
# 21. Smallest Number
# ==========================================================

print("========== Smallest Number ==========")

"""
Definition:
This program finds the smallest
number in a list.
"""

numbers = [45, 12, 89, 23, 67]

smallest = min(numbers)

print("List             :", numbers)
print("Smallest Number  :", smallest)

print()


# ==========================================================
# 22. Find Even Numbers
# ==========================================================

print("========== Find Even Numbers ==========")

"""
Definition:
Print all even numbers
from a list.
"""

numbers = [10, 15, 20, 25, 30, 35, 40]

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
from a list.
"""

numbers = [10, 15, 20, 25, 30, 35, 40]

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
numbers in a list.
"""

numbers = [10, -5, 30, -20, 15, -1, 0]

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
Search for an element
inside a list.
"""

numbers = [5, 10, 15, 20, 25]

search = int(input("Enter Number to Search: "))

if search in numbers:
    print(search, "Found in List")

else:
    print(search, "Not Found")

print()


# ==========================================================
# 26. Reverse a List
# ==========================================================

print("========== Reverse a List ==========")

"""
Definition:
Reverse all elements
of a list.
"""

numbers = [10, 20, 30, 40, 50]

print("Original List :", numbers)

numbers.reverse()

print("Reversed List :", numbers)

print()


# ==========================================================
# 27. Remove Duplicates
# ==========================================================

print("========== Remove Duplicates ==========")

"""
Definition:
Remove duplicate values
from a list.
"""

numbers = [10, 20, 10, 30, 40, 20, 50]

unique_numbers = list(set(numbers))

print("Original List :", numbers)
print("Unique List   :", unique_numbers)

print()


# ==========================================================
# 28. Second Largest Number
# ==========================================================

print("========== Second Largest Number ==========")

"""
Definition:
Find the second largest
number in a list.
"""

numbers = [10, 50, 20, 80, 40, 60]

numbers.sort()

print("List :", numbers)
print("Second Largest :", numbers[-2])

print()


# ==========================================================
# 29. Find Maximum & Minimum
# ==========================================================

print("========== Maximum & Minimum ==========")

"""
Definition:
Find the maximum and minimum
values from a list.
"""

numbers = [25, 15, 80, 10, 45]

print("Maximum :", max(numbers))
print("Minimum :", min(numbers))

print()


# ==========================================================
# 30. Average of List
# ==========================================================

print("========== Average of List ==========")

"""
Definition:
Calculate the average
of all numbers in a list.
"""

numbers = [10, 20, 30, 40, 50]

average = sum(numbers) / len(numbers)

print("List    :", numbers)
print("Average :", average)

print()

# ==========================================================
# 31. Student Marks Management System
# ==========================================================

print("========== Student Marks Management System ==========")

"""
Definition:
Store student marks in a list and calculate
Total, Average, Maximum, and Minimum marks.
"""

marks = []

for i in range(5):
    mark = float(input(f"Enter Marks of Subject {i + 1}: "))
    marks.append(mark)

print("\nStudent Marks :", marks)
print("Total Marks   :", sum(marks))
print("Average Marks :", sum(marks) / len(marks))
print("Highest Marks :", max(marks))
print("Lowest Marks  :", min(marks))

print()


# ==========================================================
# 32. Shopping Cart
# ==========================================================

print("========== Shopping Cart ==========")

"""
Definition:
A simple shopping cart where the user
can add items until they type 'done'.
"""

cart = []

while True:

    item = input("Enter Item (type 'done' to finish): ")

    if item.lower() == "done":
        break

    cart.append(item)

print("\nShopping Cart Items:")

for item in cart:
    print("-", item)

print("Total Items :", len(cart))

print()


# ==========================================================
# 33. To-Do List
# ==========================================================

print("========== To-Do List ==========")

"""
Definition:
Create a simple to-do list using Python lists.
"""

tasks = []

while True:

    task = input("Enter Task (type 'done' to finish): ")

    if task.lower() == "done":
        break

    tasks.append(task)

print("\nYour To-Do List:")

for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

print()


# ==========================================================
# 34. Contact Book
# ==========================================================

print("========== Contact Book ==========")

"""
Definition:
Store contact names and phone numbers
using nested lists.
"""

contacts = []

for i in range(3):

    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    contacts.append([name, phone])

print("\nSaved Contacts:")

for contact in contacts:
    print("Name :", contact[0], "| Phone :", contact[1])

print()


# ==========================================================
# 35. Employee Record System
# ==========================================================

print("========== Employee Record System ==========")

"""
Definition:
Store employee records using nested lists.
"""

employees = []

for i in range(3):

    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")
    emp_salary = float(input("Enter Employee Salary: "))

    employees.append([emp_id, emp_name, emp_salary])

print("\nEmployee Records")

for employee in employees:

    print("----------------------------")
    print("ID     :", employee[0])
    print("Name   :", employee[1])
    print("Salary :", employee[2])

print()


# ==========================================================
# 36. Quiz
# ==========================================================

print("========== Python List Quiz ==========")

print("Q1. Which data type is mutable?")
print("a) Tuple")
print("b) List")
print("c) String")
print("d) Integer")

answer = input("Enter Your Answer: ").lower()

if answer == "b":
    print("Correct Answer!")

else:
    print("Wrong Answer!")
    print("Correct Answer: b) List")

print()

print("Q2. Which method is used to add one item at the end of a list?")
print("a) insert()")
print("b) extend()")
print("c) append()")
print("d) remove()")

answer = input("Enter Your Answer: ").lower()

if answer == "c":
    print("Correct Answer!")

else:
    print("Wrong Answer!")
    print("Correct Answer: c) append()")

print()

print("Q3. Which function returns the length of a list?")
print("a) size()")
print("b) count()")
print("c) len()")
print("d) length()")

answer = input("Enter Your Answer: ").lower()

if answer == "c":
    print("Correct Answer!")

else:
    print("Wrong Answer!")
    print("Correct Answer: c) len()")

print()

