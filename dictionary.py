"""
==================================================
Python Dictionaries
File: 16_Dictionary.py

Topics Covered:
1. What is a Dictionary?
2. Why Use Dictionaries?
3. Creating a Dictionary
4. Dictionary Data Types
5. Access Dictionary Items
6. Access Using get()
7. Dictionary Keys
8. Dictionary Values
9. Dictionary Items
10. Change Dictionary Items
11. Add Dictionary Items
12. Remove Dictionary Items
    - pop()
    - popitem()
    - del
    - clear()
13. Check Key Exists (in)
14. Dictionary Length (len())
15. Loop Through a Dictionary
16. Nested Dictionaries
17. Copy a Dictionary
18. Join Dictionaries
19. Dictionary Methods
    - keys()
    - values()
    - items()
    - update()
    - get()
20. Difference Between List, Tuple, and Dictionary

Author : Eishaa
Language : Python
==================================================
"""

# ==========================================================
# Python Dictionaries
# ==========================================================

print("========== Python Dictionaries ==========\n")

# ==========================================================
# 1. What is a Dictionary?
# ==========================================================

"""
Definition:
A Dictionary is a collection of key-value pairs.
It is ordered, mutable (changeable), and keys
must be unique.
"""

# ==========================================================
# 2. Why Use Dictionaries?
# ==========================================================

"""
Advantages of Dictionaries

1. Store data as key-value pairs
2. Fast data lookup
3. Mutable (can be modified)
4. Easy to update
5. Keys are unique
"""

# ==========================================================
# 3. Creating a Dictionary
# ==========================================================

print("========== Creating a Dictionary ==========")

student = {
    "name": "Ali",
    "age": 20,
    "course": "Python"
}

print(student)

print()

# ==========================================================
# 4. Dictionary Data Types
# ==========================================================

print("========== Dictionary Data Types ==========")

data = {
    "integer": 10,
    "float": 20.5,
    "string": "Python",
    "boolean": True,
    "list": [1, 2, 3]
}

print(data)

print()

# ==========================================================
# 5. Access Dictionary Items
# ==========================================================

print("========== Access Dictionary Items ==========")

student = {
    "name": "Ali",
    "age": 20,
    "course": "Python"
}

print("Name   :", student["name"])
print("Course :", student["course"])

print()

# ==========================================================
# 6. Access Using get()
# ==========================================================

print("========== Access Using get() ==========")

print(student.get("age"))
print(student.get("name"))

print()

# ==========================================================
# 7. Dictionary Keys
# ==========================================================

print("========== Dictionary Keys ==========")

print(student.keys())

print()

# ==========================================================
# 8. Dictionary Values
# ==========================================================

print("========== Dictionary Values ==========")

print(student.values())

print()

# ==========================================================
# 9. Dictionary Items
# ==========================================================

print("========== Dictionary Items ==========")

print(student.items())

print()

# ==========================================================
# 10. Change Dictionary Items
# ==========================================================

print("========== Change Dictionary Items ==========")

student["age"] = 21

print(student)

print()

# ==========================================================
# 11. Add Dictionary Items
# ==========================================================

print("========== Add Dictionary Items ==========")

student["city"] = "Karachi"

print(student)

print()

# ==========================================================
# 12. Remove Dictionary Items
# ==========================================================

print("========== pop() ==========")

student.pop("city")

print(student)

print()

print("========== popitem() ==========")

student.popitem()

print(student)

print()

print("========== del ==========")

student["gender"] = "Male"

print("Before :", student)

del student["gender"]

print("After  :", student)

print()

print("========== clear() ==========")

temp = {
    "A": 1,
    "B": 2
}

print("Before :", temp)

temp.clear()

print("After  :", temp)

print()

# ==========================================================
# 13. Check Key Exists
# ==========================================================

print("========== Check Key Exists ==========")

student = {
    "name": "Ali",
    "age": 20
}

if "name" in student:
    print("Key Found")

else:
    print("Key Not Found")

print()

# ==========================================================
# 14. Dictionary Length
# ==========================================================

print("========== Dictionary Length ==========")

print("Length =", len(student))

print()

# ==========================================================
# 15. Loop Through a Dictionary
# ==========================================================

print("========== Loop Through Dictionary ==========")

for key, value in student.items():

    print(key, ":", value)

print()

# ==========================================================
# 16. Nested Dictionaries
# ==========================================================

print("========== Nested Dictionaries ==========")

students = {
    "student1": {
        "name": "Ali",
        "age": 20
    },

    "student2": {
        "name": "Sara",
        "age": 21
    }
}

print(students)

print("Student 1 Name :", students["student1"]["name"])

print()

# ==========================================================
# 17. Copy a Dictionary
# ==========================================================

print("========== Copy a Dictionary ==========")

student_copy = student.copy()

print("Original :", student)
print("Copy     :", student_copy)

print()

# ==========================================================
# 18. Join Dictionaries
# ==========================================================

print("========== Join Dictionaries ==========")

dict1 = {
    "A": 1,
    "B": 2
}

dict2 = {
    "C": 3,
    "D": 4
}

joined = dict1 | dict2

print(joined)

print()

# ==========================================================
# 19. Dictionary Methods
# ==========================================================

print("========== Dictionary Methods ==========")

person = {
    "name": "Ahmed",
    "age": 25
}

print("Keys   :", person.keys())
print("Values :", person.values())
print("Items  :", person.items())
print("Get    :", person.get("name"))

person.update({"city": "Lahore"})

print("Update :", person)

print()

# ==========================================================
# 20. Difference Between List, Tuple, and Dictionary
# ==========================================================

print("========== List vs Tuple vs Dictionary ==========")

print("List")
print("- Ordered")
print("- Mutable")
print("- Uses []")

print()

print("Tuple")
print("- Ordered")
print("- Immutable")
print("- Uses ()")

print()

print("Dictionary")
print("- Key-Value Pairs")
print("- Mutable")
print("- Uses {}")

print()

# ==========================================================
# 21. Student Information
# ==========================================================

print("========== Student Information ==========")

"""
Definition:
Store and display student information
using a dictionary.
"""

student = {
    "Name": "Ali",
    "Age": 20,
    "Course": "Python",
    "City": "Karachi"
}

for key, value in student.items():
    print(key, ":", value)

print()


# ==========================================================
# 22. Employee Information
# ==========================================================

print("========== Employee Information ==========")

"""
Definition:
Store employee details in a dictionary.
"""

employee = {
    "ID": 101,
    "Name": "Ahmed",
    "Department": "IT",
    "Salary": 75000
}

for key, value in employee.items():
    print(key, ":", value)

print()


# ==========================================================
# 23. Product Details
# ==========================================================

print("========== Product Details ==========")

"""
Definition:
Store product information using a dictionary.
"""

product = {
    "Product ID": 1001,
    "Product Name": "Laptop",
    "Price": 85000,
    "Quantity": 5
}

for key, value in product.items():
    print(key, ":", value)

print()


# ==========================================================
# 24. Count Character Frequency
# ==========================================================

print("========== Count Character Frequency ==========")

"""
Definition:
Count the frequency of each character
in a string.
"""

text = input("Enter a String: ")

frequency = {}

for char in text:

    if char in frequency:
        frequency[char] += 1

    else:
        frequency[char] = 1

print(frequency)

print()


# ==========================================================
# 25. Word Counter
# ==========================================================

print("========== Word Counter ==========")

"""
Definition:
Count the frequency of each word
in a sentence.
"""

sentence = input("Enter a Sentence: ")

words = sentence.split()

word_count = {}

for word in words:

    if word in word_count:
        word_count[word] += 1

    else:
        word_count[word] = 1

print(word_count)

print()


# ==========================================================
# 26. Search a Key
# ==========================================================

print("========== Search a Key ==========")

"""
Definition:
Search whether a key exists
in a dictionary.
"""

student = {
    "Name": "Ali",
    "Age": 20,
    "Course": "Python"
}

key = input("Enter Key to Search: ")

if key in student:
    print("Key Found")
    print("Value :", student[key])

else:
    print("Key Not Found")

print()


# ==========================================================
# 27. Update Dictionary Value
# ==========================================================

print("========== Update Dictionary Value ==========")

"""
Definition:
Update the value of an existing key.
"""

student = {
    "Name": "Ali",
    "Age": 20
}

print("Before Update")
print(student)

student["Age"] = 21

print("After Update")
print(student)

print()


# ==========================================================
# 28. Merge Two Dictionaries
# ==========================================================

print("========== Merge Two Dictionaries ==========")

"""
Definition:
Combine two dictionaries.
"""

dict1 = {
    "A": 1,
    "B": 2
}

dict2 = {
    "C": 3,
    "D": 4
}

merged = dict1 | dict2

print(merged)

print()


# ==========================================================
# 29. Find Maximum & Minimum Value
# ==========================================================

print("========== Maximum & Minimum Value ==========")

"""
Definition:
Find maximum and minimum values
from a dictionary.
"""

marks = {
    "Math": 85,
    "English": 70,
    "Science": 92,
    "Computer": 88
}

print("Maximum Marks :", max(marks.values()))
print("Minimum Marks :", min(marks.values()))

print()


# ==========================================================
# 30. Student Marks Calculator
# ==========================================================

print("========== Student Marks Calculator ==========")

"""
Definition:
Calculate total, average,
highest, and lowest marks.
"""

marks = {
    "Math": 80,
    "English": 75,
    "Science": 90,
    "Computer": 85
}

total = sum(marks.values())
average = total / len(marks)

print("Marks :", marks)
print("Total :", total)
print("Average :", average)
print("Highest :", max(marks.values()))
print("Lowest :", min(marks.values()))

print()


# ==========================================================
# 31. Phone Book
# ==========================================================

print("========== Phone Book ==========")

"""
Definition:
Store names and phone numbers
using a dictionary.
"""

phone_book = {
    "Ali": "03001234567",
    "Ahmed": "03111234567",
    "Sara": "03221234567"
}

name = input("Enter Name: ")

if name in phone_book:
    print("Phone Number :", phone_book[name])

else:
    print("Contact Not Found")

print()


# ==========================================================
# 32. Shopping Bill
# ==========================================================

print("========== Shopping Bill ==========")

"""
Definition:
Calculate the total shopping bill.
"""

cart = {
    "Milk": 250,
    "Bread": 180,
    "Eggs": 320,
    "Juice": 450
}

print("Shopping Items")

for item, price in cart.items():
    print(item, ":", price)

print()

print("Total Bill =", sum(cart.values()))

print()
# ==========================================================
# 33. Student Management System
# ==========================================================

print("========== Student Management System ==========")

"""
Definition:
Store and display student information
using a dictionary.
"""

student = {}

student["ID"] = input("Enter Student ID: ")
student["Name"] = input("Enter Student Name: ")
student["Age"] = int(input("Enter Student Age: "))
student["Course"] = input("Enter Student Course: ")

print("\n===== Student Details =====")

for key, value in student.items():
    print(key, ":", value)

print()


# ==========================================================
# 34. Library Management System
# ==========================================================

print("========== Library Management System ==========")

"""
Definition:
Store book information using dictionaries.
"""

library = {
    "Book ID": input("Enter Book ID: "),
    "Book Name": input("Enter Book Name: "),
    "Author": input("Enter Author Name: "),
    "Available": "Yes"
}

print("\n===== Library Record =====")

for key, value in library.items():
    print(key, ":", value)

print()


# ==========================================================
# 35. Employee Management System
# ==========================================================

print("========== Employee Management System ==========")

"""
Definition:
Store employee details using dictionaries.
"""

employee = {}

employee["ID"] = input("Enter Employee ID: ")
employee["Name"] = input("Enter Employee Name: ")
employee["Department"] = input("Enter Department: ")
employee["Salary"] = float(input("Enter Salary: "))

print("\n===== Employee Record =====")

for key, value in employee.items():
    print(key, ":", value)

print()


# ==========================================================
# 36. Inventory Management System
# ==========================================================

print("========== Inventory Management System ==========")

"""
Definition:
Store product inventory using dictionaries.
"""

inventory = {}

inventory["Product"] = input("Enter Product Name: ")
inventory["Price"] = float(input("Enter Product Price: "))
inventory["Quantity"] = int(input("Enter Product Quantity: "))

print("\n===== Inventory Details =====")

for key, value in inventory.items():
    print(key, ":", value)

total_value = inventory["Price"] * inventory["Quantity"]

print("Total Inventory Value :", total_value)

print()


# ==========================================================
# 37. Contact Book
# ==========================================================

print("========== Contact Book ==========")

"""
Definition:
Store and search contacts
using a dictionary.
"""

contacts = {}

for i in range(3):

    name = input("Enter Contact Name: ")
    phone = input("Enter Phone Number: ")

    contacts[name] = phone

print("\nSaved Contacts")

for name, phone in contacts.items():
    print(name, ":", phone)

print()

search = input("Search Contact: ")

if search in contacts:
    print("Phone Number :", contacts[search])

else:
    print("Contact Not Found")

print()


# ==========================================================
# 38. Python Dictionary Quiz
# ==========================================================

print("========== Python Dictionary Quiz ==========")

score = 0

print("Q1. Which brackets are used for dictionaries?")
print("a) []")
print("b) ()")
print("c) {}")
print("d) <>")

answer = input("Enter Your Answer: ").lower()

if answer == "c":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct Answer: c\n")


print("Q2. Which method returns all dictionary keys?")
print("a) values()")
print("b) keys()")
print("c) items()")
print("d) get()")

answer = input("Enter Your Answer: ").lower()

if answer == "b":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct Answer: b\n")


print("Q3. Which method returns the value of a key safely?")
print("a) get()")
print("b) update()")
print("c) pop()")
print("d) clear()")

answer = input("Enter Your Answer: ").lower()

if answer == "a":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct Answer: a\n")


print("Q4. Which method removes all items from a dictionary?")
print("a) pop()")
print("b) popitem()")
print("c) clear()")
print("d) del()")

answer = input("Enter Your Answer: ").lower()

if answer == "c":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct Answer: c\n")


print("====================================")
print("Your Final Score :", score, "/ 4")
print("====================================")

print()
