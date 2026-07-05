
# ==========================================================
# Python Object-Oriented Programming (OOP)
# ==========================================================
# 1. What is OOP?
# ==========================================================

"""
Definition:
Object-Oriented Programming (OOP) is a programming
paradigm that organizes code into objects and classes.

It makes programs more organized, reusable,
and easier to maintain.
"""

# ==========================================================
# 2. Why Use OOP?
# ==========================================================

"""
Advantages of OOP

1. Code Reusability
2. Better Organization
3. Easy Maintenance
4. Real-World Modeling
5. Improved Security
6. Easy to Debug
"""

print("Advantages of OOP")
print("- Code Reusability")
print("- Better Organization")
print("- Easy Maintenance")
print("- Real-World Modeling")
print("- Improved Security")
print("- Easy to Debug")

print()

# ==========================================================
# 3. Features of OOP
# ==========================================================

print("========== Features of OOP ==========")

print("1. Encapsulation")
print("2. Abstraction")
print("3. Inheritance")
print("4. Polymorphism")

print()

# ==========================================================
# 4. Class
# ==========================================================

"""
Definition:
A Class is a blueprint or template
for creating objects.
"""

print("========== Class ==========")

class Student:
    pass

print("Student class created successfully.")

print()

# ==========================================================
# 5. Object
# ==========================================================

"""
Definition:
An Object is an instance of a class.
"""

print("========== Object ==========")

student1 = Student()

print(student1)

print()

# ==========================================================
# 6. Difference Between Class and Object
# ==========================================================

print("========== Class vs Object ==========")

print("Class")
print("- Blueprint")
print("- Logical Entity")
print("- Used to Create Objects")

print()

print("Object")
print("- Instance of a Class")
print("- Physical Entity")
print("- Uses Class Properties")

print()

# ==========================================================
# 7. Syntax of a Class
# ==========================================================

print("========== Class Syntax ==========")

class Person:

    pass

print("Syntax Example Completed")

print()

# ==========================================================
# 8. Creating a Class
# ==========================================================

print("========== Creating a Class ==========")

class Car:

    brand = "Toyota"

print("Class Created Successfully")

print()

# ==========================================================
# 9. Creating an Object
# ==========================================================

print("========== Creating an Object ==========")

car1 = Car()

print("Brand :", car1.brand)

print()

# ==========================================================
# 10. __init__() Constructor
# ==========================================================

print("========== Constructor (__init__) ==========")

class Employee:

    def __init__(self):

        print("Constructor Called")

employee1 = Employee()

print()

# ==========================================================
# 11. self Keyword
# ==========================================================

print("========== self Keyword ==========")

"""
Definition:
self refers to the current object
of the class.
"""

class Teacher:

    def show(self):

        print("self refers to the current object.")

teacher1 = Teacher()

teacher1.show()

print()

# ==========================================================
# 12. Instance Variables (Attributes)
# ==========================================================

print("========== Instance Variables ==========")

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

student1 = Student("Ali", 20)

print("Name :", student1.name)
print("Age  :", student1.age)

print()

# ==========================================================
# 13. Instance Methods
# ==========================================================

print("========== Instance Methods ==========")

class Student:

    def __init__(self, name):

        self.name = name

    def display(self):

        print("Student Name :", self.name)

student1 = Student("Ahmed")

student1.display()

print()

# ==========================================================
# 14. Creating Multiple Objects
# ==========================================================

print("========== Multiple Objects ==========")

student1 = Student("Ali")
student2 = Student("Sara")
student3 = Student("Esha")

student1.display()
student2.display()
student3.display()

print()

# ==========================================================
# 15. Accessing Object Attributes
# ==========================================================

print("========== Access Object Attributes ==========")

class Laptop:

    def __init__(self, brand):

        self.brand = brand

laptop1 = Laptop("Dell")

print("Laptop Brand :", laptop1.brand)

print()

# ==========================================================
# 16. Modifying Object Attributes
# ==========================================================

print("========== Modify Object Attributes ==========")

class Mobile:

    def __init__(self, brand):

        self.brand = brand

mobile1 = Mobile("Samsung")

print("Before :", mobile1.brand)

mobile1.brand = "Apple"

print("After  :", mobile1.brand)

print()
