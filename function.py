# ==========================================================
# Python Functions
# ==========================================================

print("========== Python Functions ==========\n")

# ==========================================================
# 1. What is a Function?
# ==========================================================

"""
Definition:
A Function is a reusable block of code that performs
a specific task. It helps avoid code repetition and
makes programs easier to read and maintain.
"""

# ==========================================================
# 2. Why Use Functions?
# ==========================================================

"""
Advantages of Functions

1. Reduce Code Repetition
2. Improve Code Readability
3. Easy to Debug
4. Easy to Reuse
5. Better Program Organization
"""

# ==========================================================
# 3. Function Syntax
# ==========================================================

"""
Syntax:

def function_name():
    # Code

function_name()
"""

# ==========================================================
# 4. Creating a Function
# ==========================================================

print("========== Creating a Function ==========")

def welcome():
    print("Welcome to Python Functions")

welcome()

print()

# ==========================================================
# 5. Calling a Function
# ==========================================================

print("========== Calling a Function ==========")

def greeting():
    print("Hello, Python!")

greeting()
greeting()
greeting()

print()

# ==========================================================
# 6. Function Without Parameters
# ==========================================================

print("========== Function Without Parameters ==========")

def student():

    print("Name : Eishaa")
    print("Course : Python")

student()

print()

# ==========================================================
# 7. Function With Parameters
# ==========================================================

print("========== Function With Parameters ==========")

def greet(name):

    print("Welcome", name)

greet("Ali")
greet("Ahmed")
greet("Sara")

print()

# ==========================================================
# 8. Function With Multiple Parameters
# ==========================================================

print("========== Function With Multiple Parameters ==========")

def student_info(name, age):

    print("Name :", name)
    print("Age  :", age)

student_info("Ali", 20)

print()

# ==========================================================
# 9. Default Parameters
# ==========================================================

print("========== Default Parameters ==========")

def country(name, country="Pakistan"):

    print(name, "lives in", country)

country("Ali")
country("John", "USA")

print()

# ==========================================================
# 10. Keyword Arguments
# ==========================================================

print("========== Keyword Arguments ==========")

def employee(name, salary):

    print("Name   :", name)
    print("Salary :", salary)

employee(salary=50000, name="Ahmed")

print()

# ==========================================================
# 11. Positional Arguments
# ==========================================================

print("========== Positional Arguments ==========")

def add(a, b):

    print("Addition =", a + b)

add(10, 20)

print()

# ==========================================================
# 12. return Statement
# ==========================================================

print("========== return Statement ==========")

def square(number):

    return number ** 2

result = square(5)

print("Square =", result)

print()

# ==========================================================
# 13. Local Variables
# ==========================================================

print("========== Local Variables ==========")

def demo():

    message = "I am a Local Variable"

    print(message)

demo()

print()

# ==========================================================
# 14. Global Variables
# ==========================================================

print("========== Global Variables ==========")

message = "I am a Global Variable"

def show():

    print(message)

show()

print()
# ==========================================================
# 15. Addition Function
# ==========================================================

print("========== Addition Function ==========")

"""
Definition:
This function takes two numbers as input
and returns their sum.
"""

def addition(num1, num2):
    return num1 + num2

number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))

result = addition(number1, number2)

print("Addition =", result)

print()


# ==========================================================
# 16. Even/Odd Function
# ==========================================================

print("========== Even/Odd Function ==========")

"""
Definition:
This function checks whether
a number is Even or Odd.
"""

def even_odd(number):

    if number % 2 == 0:
        return "Even Number"

    else:
        return "Odd Number"

number = int(input("Enter a Number: "))

print(even_odd(number))

print()


# ==========================================================
# 17. Largest Number Function
# ==========================================================

print("========== Largest Number Function ==========")

"""
Definition:
This function returns the
largest of two numbers.
"""

def largest(num1, num2):

    if num1 > num2:
        return num1

    else:
        return num2

first = int(input("Enter First Number: "))
second = int(input("Enter Second Number: "))

print("Largest Number =", largest(first, second))

print()


# ==========================================================
# 18. Prime Number Function
# ==========================================================

print("========== Prime Number Function ==========")

"""
Definition:
A Prime Number has exactly
two factors: 1 and itself.
"""

def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, number):

        if number % i == 0:
            return False

    return True

number = int(input("Enter a Number: "))

if is_prime(number):
    print(number, "is a Prime Number")

else:
    print(number, "is Not a Prime Number")

print()


# ==========================================================
# 19. Factorial Function
# ==========================================================

print("========== Factorial Function ==========")

"""
Definition:
Factorial is the product of all
positive integers up to a given number.

Example:
5! = 120
"""

def factorial(number):

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result

number = int(input("Enter a Number: "))

print("Factorial =", factorial(number))

print()

# =============MINI PROJECTS================================

# ==========================================================
# 20. Calculator Using Functions
# ==========================================================

print("========== Calculator Using Functions ==========")

"""
Definition:
A simple calculator using
multiple functions.
"""

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):

    if b != 0:
        return a / b

    return "Cannot Divide by Zero"


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Choose an Option (1-4): ")

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

if choice == "1":
    print("Answer =", add(num1, num2))

elif choice == "2":
    print("Answer =", subtract(num1, num2))

elif choice == "3":
    print("Answer =", multiply(num1, num2))

elif choice == "4":
    print("Answer =", divide(num1, num2))

else:
    print("Invalid Choice")

print()
# ==========================================================
# 21. Student Result System
# ==========================================================

print("========== Student Result System ==========")

"""
Definition:
This function calculates the total marks,
percentage, grade, and pass/fail status.
"""

def student_result():

    name = input("Enter Student Name: ")

    sub1 = float(input("Enter Subject 1 Marks: "))
    sub2 = float(input("Enter Subject 2 Marks: "))
    sub3 = float(input("Enter Subject 3 Marks: "))

    total = sub1 + sub2 + sub3
    percentage = total / 3

    if percentage >= 80:
        grade = "A"

    elif percentage >= 70:
        grade = "B"

    elif percentage >= 60:
        grade = "C"

    elif percentage >= 50:
        grade = "D"

    else:
        grade = "Fail"

    print("\n===== Result =====")
    print("Student :", name)
    print("Total :", total)
    print("Percentage :", percentage)
    print("Grade :", grade)

student_result()

print()


# ==========================================================
# 22. Positive, Negative or Zero Function
# ==========================================================

print("========== Positive, Negative or Zero ==========")

"""
Definition:
This function checks whether a number is
Positive, Negative, or Zero.
"""

def check_number(number):

    if number > 0:
        return "Positive Number"

    elif number < 0:
        return "Negative Number"

    else:
        return "Zero"

number = int(input("Enter a Number: "))

print(check_number(number))

print()


# ==========================================================
# 23. Traffic Light Function
# ==========================================================

print("========== Traffic Light Function ==========")

"""
Definition:
This function displays the action
based on the selected traffic light color.
"""

def traffic_light(color):

    color = color.lower()

    if color == "red":
        return "Stop"

    elif color == "yellow":
        return "Ready"

    elif color == "green":
        return "Go"

    else:
        return "Invalid Color"

color = input("Enter Traffic Light Color (Red, Yellow, Green): ")

print(traffic_light(color))

print()


# ==========================================================
# 24. Employee Salary Calculator
# ==========================================================

print("========== Employee Salary Calculator ==========")

"""
Definition:
This function calculates the total salary
after adding the bonus.
"""

def salary_calculator(basic_salary, bonus):

    total_salary = basic_salary + bonus

    return total_salary

salary = float(input("Enter Basic Salary: "))
bonus = float(input("Enter Bonus: "))

print("Total Salary =", salary_calculator(salary, bonus))

print()


# ==========================================================
# 25. Bank Account System
# ==========================================================

print("========== Bank Account System ==========")

"""
Definition:
Simple Deposit and Withdraw System
using Functions.
"""

balance = 5000

def deposit(amount):

    global balance

    balance += amount

    print("Updated Balance =", balance)


def withdraw(amount):

    global balance

    if amount <= balance:

        balance -= amount

        print("Remaining Balance =", balance)

    else:

        print("Insufficient Balance")


deposit(1000)

withdraw(2000)

print()


# ==========================================================
# 26. ATM System Using Functions
# ==========================================================

print("========== ATM System ==========")

"""
Definition:
A simple ATM Machine using Functions.
"""

balance = 10000

def check_balance():
    print("Current Balance =", balance)


def withdraw_money(amount):

    global balance

    if amount <= balance:

        balance -= amount

        print("Remaining Balance =", balance)

    else:

        print("Insufficient Balance")


def deposit_money(amount):

    global balance

    balance += amount

    print("Updated Balance =", balance)


check_balance()

deposit_money(2000)

withdraw_money(3000)

print()



