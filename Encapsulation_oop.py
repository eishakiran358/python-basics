
#               Python OOP - Encapsulation 
# ==========================================================
# 1. What is Encapsulation?
# ==========================================================

"""
Definition:

Encapsulation is one of the four main principles of
Object-Oriented Programming (OOP).

Encapsulation means wrapping (binding) data (variables)
and methods (functions) together into a single unit
called a Class.

It also protects data by hiding it from direct access.

Simple Definition:

Encapsulation = Data + Methods + Data Hiding
"""

# ==========================================================
# 2. Why Use Encapsulation?
# ==========================================================

"""
We use Encapsulation because:

✔ It protects data.
✔ Prevents unauthorized access.
✔ Makes code more secure.
✔ Makes programs easier to maintain.
✔ Improves code reusability.
✔ Reduces bugs.
"""

# ==========================================================
# 3. Advantages of Encapsulation
# ==========================================================

"""
Advantages

1. Data Hiding
2. Better Security
3. Easy Maintenance
4. Code Reusability
5. Better Control of Data
6. Easy Debugging
7. Professional Code Structure
"""

# ==========================================================
# 4. Public Members
# ==========================================================

"""
Public Members

Public variables can be accessed
from anywhere inside or outside the class.

Syntax

self.variable_name
"""

print("========== Public Members ==========\n")


class Student:

    # Constructor
    def __init__(self, name, age):

        # Public Variables
        self.name = name
        self.age = age

    # Public Method
    def display(self):

        print("Student Name :", self.name)
        print("Student Age  :", self.age)


# Create Object
student1 = Student("Eishaa", 21)

# Access Public Variables Directly
print(student1.name)
print(student1.age)

# Call Public Method
student1.display()

print("\n")

# ==========================================================
# Explanation
# ==========================================================

"""
Explanation

self.name
self.age

These are Public Variables.

Since they are public,
we can access them directly
using the object.

Example

student1.name
student1.age
"""

# ==========================================================
# 5. Private Members
# ==========================================================

"""
Private Members

Private variables cannot be accessed
directly from outside the class.

Syntax

self.__variable_name

(Double Underscore __)
"""

print("========== Private Members ==========\n")


class Employee:

    # Constructor
    def __init__(self, name, salary):

        # Private Variables
        self.__name = name
        self.__salary = salary

    # Public Method
    def display(self):

        print("Employee Name  :", self.__name)
        print("Employee Salary:", self.__salary)


# Create Object
employee1 = Employee("Ali", 80000)

# Access Through Method
employee1.display()

# Direct Access (Not Allowed)

# print(employee1.__name)
# print(employee1.__salary)

# These lines will generate an AttributeError.


print("\n")

# ==========================================================
# Explanation
# ==========================================================

"""
Private Variables start with
Double Underscore (__).

Example

self.__name
self.__salary

They cannot be accessed directly.

Correct Way

employee1.display()

Wrong Way

employee1.__name

Output

AttributeError
"""

# ==========================================================
# 6. Simple Encapsulation Example
# ==========================================================

"""
Example:

A Bank stores money privately.

Customers cannot directly
change the balance.

Instead, they use methods like

deposit()

withdraw()

check_balance()

This is called Encapsulation.
"""

print("========== Simple Encapsulation Example ==========\n")


class Bank:

    # Constructor
    def __init__(self):

        # Private Variable
        self.__balance = 10000

    # Deposit Method
    def deposit(self, amount):

        self.__balance += amount

        print(f"Rs.{amount} Deposited Successfully.")

    # Check Balance
    def check_balance(self):

        print("Current Balance :", self.__balance)


# Create Object
account = Bank()

# Deposit Money
account.deposit(5000)

# Check Balance
account.check_balance()

# Direct Access (Not Allowed)

# print(account.__balance)

print("\n")


# ==========================================================
# Project 1 : Student Class
# ==========================================================

"""
Problem Statement

Create a Student class with the following requirements.

Private Variables
-----------------
__name
__age
__marks

Methods
-------
display_student()
set_marks()
get_marks()
"""

print("\n========== Student Class ==========\n")


class Student:

    # Constructor
    def __init__(self, name, age, marks):

        # Private Variables
        self.__name = name
        self.__age = age
        self.__marks = marks

    # Display Student Details
    def display_student(self):

        print("Student Name :", self.__name)
        print("Student Age  :", self.__age)
        print("Student Marks:", self.__marks)

    # Update Marks
    def set_marks(self, marks):

        if 0 <= marks <= 100:

            self.__marks = marks
            print("Marks Updated Successfully.")

        else:

            print("Invalid Marks.")

    # Get Marks
    def get_marks(self):

        return self.__marks


# Create Object
student1 = Student("Eishaa", 21, 90)

student1.display_student()

student1.set_marks(95)

print("Updated Marks :", student1.get_marks())


# ==========================================================
# Project 2 : Bank Account Class
# ==========================================================

"""
Problem Statement

Create a BankAccount class.

Private Variables
-----------------
__account_number
__holder_name
__balance

Methods
-------
deposit()
withdraw()
check_balance()
"""

print("\n========== Bank Account ==========\n")


class BankAccount:

    # Constructor
    def __init__(self, account_number, holder_name, balance):

        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    # Deposit Money
    def deposit(self, amount):

        if amount > 0:

            self.__balance += amount
            print(f"Rs.{amount} Deposited Successfully.")

        else:

            print("Invalid Amount.")

    # Withdraw Money
    def withdraw(self, amount):

        if amount <= self.__balance:

            self.__balance -= amount
            print(f"Rs.{amount} Withdrawn Successfully.")

        else:

            print("Insufficient Balance.")

    # Check Balance
    def check_balance(self):

        print("Current Balance :", self.__balance)


# Create Object
account1 = BankAccount("ACC101", "Eishaa", 10000)

account1.deposit(5000)

account1.withdraw(3000)

account1.check_balance()


# ==========================================================
# Project 3 : Employee Class
# ==========================================================

"""
Problem Statement

Create an Employee class.

Private Variables
-----------------
__id
__name
__salary

Methods
-------
display_employee()
increase_salary()
"""

print("\n========== Employee Class ==========\n")


class Employee:

    # Constructor
    def __init__(self, emp_id, name, salary):

        self.__id = emp_id
        self.__name = name
        self.__salary = salary

    # Display Details
    def display_employee(self):

        print("Employee ID :", self.__id)
        print("Employee Name :", self.__name)
        print("Employee Salary :", self.__salary)

    # Increase Salary
    def increase_salary(self, amount):

        if amount > 0:

            self.__salary += amount

            print(f"Salary Increased by Rs.{amount}")

        else:

            print("Invalid Amount")


# Create Object
employee1 = Employee(101, "Ali", 70000)

employee1.display_employee()

employee1.increase_salary(10000)

employee1.display_employee()
print("\n========== Product Management System ==========\n")


class Product:

    # Constructor
    def __init__(self, product_name, price, stock):

        # Private Variables
        self.__product_name = product_name
        self.__price = price
        self.__stock = stock

    # Display Product Details
    def display_product(self):

        print("Product Name :", self.__product_name)
        print("Price        :", self.__price)
        print("Stock        :", self.__stock)

    # Sell Product
    def sell(self, quantity):

        if quantity <= 0:
            print("Quantity must be greater than 0.")

        elif quantity > self.__stock:
            print("Insufficient Stock.")

        else:
            self.__stock -= quantity
            print(f"{quantity} Product(s) Sold Successfully.")

    # Restock Product
    def restock(self, quantity):

        if quantity > 0:

            self.__stock += quantity
            print(f"{quantity} Product(s) Added Successfully.")

        else:

            print("Invalid Quantity.")


# Create Object

product1 = Product("Laptop", 120000, 10)

product1.display_product()

product1.sell(3)

product1.restock(5)

product1.display_product()


# ==========================================================
# Project 5 : ATM System
# ==========================================================

"""
Problem Statement

Create an ATM class.

Private Variables
-----------------
__pin
__balance

Methods
-------
deposit()
withdraw()
change_pin()
check_balance()
"""

print("\n========== ATM System ==========\n")


class ATM:

    # Constructor
    def __init__(self, pin, balance):

        self.__pin = pin
        self.__balance = balance

    # Deposit
    def deposit(self, amount):

        if amount > 0:

            self.__balance += amount

            print(f"Rs.{amount} Deposited Successfully.")

        else:

            print("Invalid Amount.")

    # Withdraw
    def withdraw(self, amount, pin):

        if pin != self.__pin:

            print("Incorrect PIN.")

        elif amount > self.__balance:

            print("Insufficient Balance.")

        else:

            self.__balance -= amount

            print(f"Rs.{amount} Withdrawn Successfully.")

    # Check Balance
    def check_balance(self, pin):

        if pin == self.__pin:

            print("Current Balance :", self.__balance)

        else:

            print("Incorrect PIN.")

    # Change PIN
    def change_pin(self, old_pin, new_pin):

        if old_pin == self.__pin:

            self.__pin = new_pin

            print("PIN Changed Successfully.")

        else:

            print("Incorrect Old PIN.")


# Create Object

atm1 = ATM(1234, 50000)

atm1.deposit(5000)

atm1.withdraw(3000, 1234)

atm1.check_balance(1234)

atm1.change_pin(1234, 5678)

atm1.check_balance(5678)

# ==========================================================
# Practice Programs - Encapsulation

# ==========================================================

# ==========================================================
# Program 1: Student Class
# Problem:
# Create a Student class with private variables
# (__name, __marks) and display them using methods.
# ==========================================================

class Student:

    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    # Getter Method
    def get_name(self):
        return self.__name

    # Getter Method
    def get_marks(self):
        return self.__marks


student1 = Student("Eishaa", 98)

print("Student Name :", student1.get_name())
print("Student Marks:", student1.get_marks())


# ==========================================================
# Program 2: Employee Salary
# Problem:
# Create an Employee class with a private salary
# variable and access it using a getter method.
# ==========================================================

class Employee:

    def __init__(self, salary):
        self.__salary = salary

    # Getter Method
    def get_salary(self):
        return self.__salary


employee1 = Employee(50000)

print("\nEmployee Salary :", employee1.get_salary())


# ==========================================================
# Program 3: Bank Account
# Problem:
# Create a BankAccount class with a private balance.
# Use getter and setter methods.
# ==========================================================

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, balance):
        self.__balance = balance


account1 = BankAccount(21000)

print("\nCurrent Balance :", account1.get_balance())

account1.set_balance(35000)

print("Updated Balance :", account1.get_balance())


# ==========================================================
# Program 4: Person Age
# Problem:
# Create a Person class with a protected variable
# (_age) and display it.
# ==========================================================

class Person:

    def __init__(self, age):
        self._age = age

    def display_age(self):
        print("\nPerson Age :", self._age)


person1 = Person(21)

person1.display_age()


# ==========================================================
# Program 5: Car Speed
# Problem:
# Create a Car class with a private speed variable.
# Use methods to set and display the speed.
# ==========================================================

class Car:

    def __init__(self, speed):
        self.__speed = speed

    # Setter
    def set_speed(self, speed):
        self.__speed = speed

    # Getter
    def get_speed(self):
        return self.__speed


car1 = Car(200)

print("\nCurrent Speed :", car1.get_speed())

car1.set_speed(250)

print("Updated Speed :", car1.get_speed())