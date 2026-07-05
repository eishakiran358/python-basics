# ==========================================================
# Project 1: Student Class
# ==========================================================

class Student:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Display Method
    def display(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")

# Object Creation
student1 = Student("Eishaa", 21)

student1.display()

# ==========================================================
# Project 2: Book Class
# ==========================================================
# Create Book Class
# ==========================================================

class Book:

    # Constructor
    # Automatically runs when an object is created.
    def __init__(self, title, author, price):

        # Instance Variables (Attributes)
        self.title = title
        self.author = author
        self.price = price

    # Method to Display Book Information
    def display_info(self):

        print("\n===== Book Information =====")
        print("Book Title :", self.title)
        print("Author     :", self.author)
        print("Price      :", self.price)


# ==========================================================
# Create Objects
# ==========================================================

book1 = Book("Artificial Intelligence", "John McCarthy", 2000)
book2 = Book("Python Programming", "Guido van Rossum", 1500)
# ==========================================================
# Call Methods
# ==========================================================

book1.display_info()

book2.display_info()

# ==========================================================
# Project 3: Rectangle Class
# ==========================================================
# Create Rectangle Class
# ==========================================================

class Rectangle:

    # Constructor
    def __init__(self, length, width):

        # Instance Variables
        self.length = length
        self.width = width

    # Calculate Area
    def area(self):

        return self.length * self.width

    # Calculate Perimeter
    def perimeter(self):

        return 2 * (self.length + self.width)

    # Check Whether Rectangle is Square
    def is_square(self):

        return self.length == self.width


# ==========================================================
# User Input

length = float(input("Enter Length: "))
width = float(input("Enter Width : "))
# Create Object

rectangle1 = Rectangle(length, width)
# Display Results

print("\n========== Rectangle Details ==========")

print("Length      :", rectangle1.length)
print("Width       :", rectangle1.width)

print("Area        :", rectangle1.area())

print("Perimeter   :", rectangle1.perimeter())

if rectangle1.is_square():

    print("Shape       : Square")

else:

    print("Shape       : Rectangle")

    # ==========================================================
# Project 4: Bank Account Class
# ==========================================================

"""
Definition:
The BankAccount class is used to manage a customer's
bank account. It allows depositing money, withdrawing
money, checking the balance, and displaying account details.

# BankAccount class
# Properties: account_number, holder_name, balance (private concept but abhi simple)
# Methods: deposit(amount), withdraw(amount), get_balance(), display_details()

"""

# ==========================================================
# Create BankAccount Class
# ==========================================================

class BankAccount:

    # Constructor
    def __init__(self, account_number, holder_name, balance):

        # Instance Variables
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    # Deposit Money
    def deposit(self, amount):

        if amount > 0:

            self.balance += amount
            print(f"Rs.{amount} deposited successfully.")

        else:

            print("Invalid Deposit Amount.")

    # Withdraw Money
    def withdraw(self, amount):

        if amount <= 0:

            print("Invalid Withdrawal Amount.")

        elif amount > self.balance:

            print("Insufficient Balance.")

        else:

            self.balance -= amount
            print(f"Rs.{amount} withdrawn successfully.")

    # Check Balance
    def get_balance(self):

        print("Current Balance:", self.balance)

    # Display Account Details
    def display_details(self):

        print("\n========== Account Details ==========")
        print("Account Number :", self.account_number)
        print("Holder Name    :", self.holder_name)
        print("Balance        :", self.balance)


# ==========================================================
# Create Object
# ==========================================================

account1 = BankAccount("ACC101", "Eishaa", 5000)

# ==========================================================
# Display Details
# ==========================================================

account1.display_details()
# Deposit Money
deposit_amount = float(input("\nEnter Deposit Amount: "))
account1.deposit(deposit_amount)

# Withdraw Money


withdraw_amount = float(input("\nEnter Withdraw Amount: "))
account1.withdraw(withdraw_amount)

account1.get_balance()


# ==========================================================
# Project 5: Employee Management System

# Create Employee Class

class Employee:

    # Constructor
    # This method automatically runs when an object is created.
    def __init__(self, emp_id, name, department, salary):

        # Instance Variables (Attributes)
        # Store the values inside the object.
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    # ======================================================
    # Display Employee Details
    # ======================================================

    def display_details(self):

        print("\n========== Employee Details ==========")
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Department  :", self.department)
        print("Salary      :", self.salary)

    # ======================================================
    # Increase Employee Salary
    # ======================================================

    def increase_salary(self, amount):

        # Check if amount is greater than zero.
        if amount > 0:

            # Increase salary
            self.salary += amount

            print(f"\nSalary increased by Rs.{amount}")

        else:

            print("Invalid Amount")

    # ======================================================
    # Change Employee Department
    # ======================================================

    def change_department(self, new_department):

        # Update department
        self.department = new_department

        print(f"\nDepartment changed to {self.department}")


# ==========================================================
# Create Employee Object
# ==========================================================

employee1 = Employee(
    101,
    "Eishaa",
    "AI Engineer",
    80000
)

# ==========================================================
# Display Employee Details
# ==========================================================

employee1.display_details()

# ==========================================================
# Increase Salary
# ==========================================================

employee1.increase_salary(10000)

# ==========================================================
# Change Department
# ==========================================================

employee1.change_department("Generative AI Engineer")

# ==========================================================
# Display Updated Details
# ==========================================================

employee1.display_details()


# ==========================================================
# Project 6: Car Management System
# ==========================================================

"""
Problem Statement:

Create a Car class with the following requirements:

Properties:
- Brand
- Model
- Color
- Price

Methods:
1. display_details()
   → Display all car information.

2. start_engine()
   → Print that the engine has started.

3. stop_engine()
   → Print that the engine has stopped.

4. update_price(new_price)
   → Update the car price.
"""
# ==========================================================
# Create Car Class
# ==========================================================

class Car:

    # Constructor
    # Automatically executes when an object is created.
    def __init__(self, brand, model, color, price):

        # Instance Variables (Attributes)
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

    # ======================================================
    # Display Car Details
    # ======================================================

    def display_details(self):

        print("\n========== Car Details ==========")
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Color :", self.color)
        print("Price :", self.price)

    # ======================================================
    # Start Engine
    # ======================================================

    def start_engine(self):

        print(f"\n{self.brand} {self.model} Engine Started.")

    # ======================================================
    # Stop Engine
    # ======================================================

    def stop_engine(self):

        print(f"{self.brand} {self.model} Engine Stopped.")

    # ======================================================
    # Update Car Price
    # ======================================================

    def update_price(self, new_price):

        # Check whether the new price is valid.
        if new_price > 0:

            # Update the price.
            self.price = new_price

            print(f"\nCar Price Updated Successfully to Rs.{self.price}")

        else:

            print("Invalid Price.")


# ==========================================================
# Create Car Object
# ==========================================================

car1 = Car(
    "Toyota",
    "Corolla",
    "White",
    4500000
)

# ==========================================================
# Display Car Information
# ==========================================================

car1.display_details()

# ==========================================================
# Start Car Engine
# ==========================================================

car1.start_engine()

# ==========================================================
# Update Car Price
# ==========================================================

car1.update_price(4800000)

# ==========================================================
# Display Updated Information
# ==========================================================

car1.display_details()

# ==========================================================
# Stop Car Engine
# ==========================================================

car1.stop_engine()
# ==========================================================
# Project 7: Library Management System
# ==========================================================

"""
Problem Statement:

Create a Library class with the following requirements:

Properties:
- Book Title
- Author Name
- Availability (True/False)

Methods:

1. display_book()
   → Display all book information.

2. issue_book()
   → Issue the book if available.

3. return_book()
   → Return the book to the library.
"""

# ==========================================================
# Create Library Class
# ==========================================================

class Library:

    # Constructor
    # Automatically executes when an object is created.
    def __init__(self, title, author, available):

        # Instance Variables (Attributes)
        self.title = title
        self.author = author
        self.available = available

    # ======================================================
    # Display Book Details
    # ======================================================

    def display_book(self):

        print("\n========== Book Details ==========")
        print("Book Title :", self.title)
        print("Author     :", self.author)

        if self.available:
            print("Status     : Available")

        else:
            print("Status     : Not Available")

    # ======================================================
    # Issue Book
    # ======================================================

    def issue_book(self):

        if self.available:

            self.available = False

            print(f"\n'{self.title}' has been issued successfully.")

        else:

            print(f"\nSorry! '{self.title}' is not available.")

    # ======================================================
    # Return Book
    # ======================================================

    def return_book(self):

        self.available = True

        print(f"\n'{self.title}' has been returned successfully.")


# ==========================================================
# Create Object
# ==========================================================

book1 = Library(
    "Python Programming",
    "Guido van Rossum",
    True
)

# ==========================================================
# Display Book Information
# ==========================================================

book1.display_book()

# ==========================================================
# Issue the Book
# ==========================================================

book1.issue_book()

# ==========================================================
# Display Updated Status
# ==========================================================

book1.display_book()

# ==========================================================
# Return the Book
# ==========================================================

book1.return_book()

# ==========================================================
# Display Final Status
# ==========================================================

book1.display_book()

# ==========================================================
# Project 8: Student Result Management System
# ==========================================================

"""
Problem Statement:

Create a Student class with the following requirements:

Properties:
- Student Name
- Roll Number
- Marks of Subject 1
- Marks of Subject 2
- Marks of Subject 3

Methods:

1. total_marks()
   → Calculate the total marks.

2. percentage()
   → Calculate the percentage.

3. grade()
   → Display the grade based on percentage.

4. display_result()
   → Display complete student result.
"""

# ==========================================================
# Create Student Class
# ==========================================================

class Student:

    # Constructor
    # Automatically executes when an object is created.
    def __init__(self, name, roll_no, subject1, subject2, subject3):

        # Instance Variables (Attributes)
        self.name = name
        self.roll_no = roll_no
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3

    # ======================================================
    # Calculate Total Marks
    # ======================================================

    def total_marks(self):

        return self.subject1 + self.subject2 + self.subject3

    # ======================================================
    # Calculate Percentage
    # ======================================================

    def percentage(self):

        total = self.total_marks()

        return total / 3

    # ======================================================
    # Calculate Grade
    # ======================================================

    def grade(self):

        percentage = self.percentage()

        if percentage >= 90:
            return "A+"

        elif percentage >= 80:
            return "A"

        elif percentage >= 70:
            return "B"

        elif percentage >= 60:
            return "C"

        elif percentage >= 50:
            return "D"

        else:
            return "Fail"

    # ======================================================
    # Display Complete Result
    # ======================================================

    def display_result(self):

        print("\n========== Student Result ==========")
        print("Student Name :", self.name)
        print("Roll Number  :", self.roll_no)
        print("Subject 1    :", self.subject1)
        print("Subject 2    :", self.subject2)
        print("Subject 3    :", self.subject3)
        print("Total Marks  :", self.total_marks())
        print("Percentage   :", self.percentage(), "%")
        print("Grade        :", self.grade())


# ==========================================================
# Create Student Object
# ==========================================================

student1 = Student(
    "Eishaa",
    101,
    90,
    85,
    95
)

# ==========================================================
# Display Student Result
# ==========================================================

student1.display_result()