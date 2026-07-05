# ==========================================================
# Python Exception Handling
# ==========================================================

print("========== Python Exception Handling ==========\n")

# ==========================================================
# 1. What is Exception Handling?
# ==========================================================

"""
Definition:
Exception Handling is a way to handle runtime
errors without stopping the program.
"""

# ==========================================================
# 2. Why Use Exception Handling?
# ==========================================================

"""
Advantages

1. Prevents program crashes
2. Handles unexpected errors
3. Improves user experience
4. Makes code more reliable
5. Easier debugging
"""

# ==========================================================
# 3. What is an Exception?
# ==========================================================

print("========== Exception Example ==========")

"""
Definition:
An Exception is an error that occurs
while the program is running.
"""

try:
    number = 10 / 0

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

print()

# ==========================================================
# 4. try Block
# ==========================================================

print("========== try Block ==========")

"""
Definition:
The try block contains the code
that may generate an exception.
"""

try:
    number = int(input("Enter a Number: "))
    print("You entered:", number)

except:
    print("Invalid Input")

print()

# ==========================================================
# 5. except Block
# ==========================================================

print("========== except Block ==========")

"""
Definition:
The except block executes
when an exception occurs.
"""

try:
    result = 20 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")

print()

# ==========================================================
# 6. Multiple except Blocks
# ==========================================================

print("========== Multiple except Blocks ==========")

"""
Definition:
Use multiple except blocks
to handle different exceptions.
"""

try:

    number = int(input("Enter Number: "))
    result = 100 / number

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Number cannot be zero.")

print()

# ==========================================================
# 7. except Exception as e
# ==========================================================

print("========== except Exception as e ==========")

"""
Definition:
Catch any exception and
display its message.
"""

try:

    number = int(input("Enter Number: "))
    print(100 / number)

except Exception as error:

    print("Error:", error)

print()

# ==========================================================
# 8. else Block
# ==========================================================

print("========== else Block ==========")

"""
Definition:
The else block executes
only if no exception occurs.
"""

try:

    number = int(input("Enter Number: "))
    print("Square =", number ** 2)

except ValueError:

    print("Invalid Number")

else:

    print("Program Executed Successfully.")

print()

# ==========================================================
# 9. finally Block
# ==========================================================

print("========== finally Block ==========")

"""
Definition:
The finally block always executes,
whether an exception occurs or not.
"""

try:

    number = int(input("Enter Number: "))
    print(100 / number)

except Exception as error:

    print(error)

finally:

    print("Program Finished.")

print()

# ==========================================================
# 10. raise Keyword
# ==========================================================

print("========== raise Keyword ==========")

"""
Definition:
Use raise to create
your own exception.
"""

age = int(input("Enter Age: "))

try:

    if age < 18:
        raise ValueError("Age must be at least 18.")

    print("Access Granted")

except ValueError as error:

    print(error)

print()

# ==========================================================
# 11. User Defined Exception
# ==========================================================

print("========== User Defined Exception ==========")

"""
Definition:
Create your own exception
using a custom class.
"""

class InvalidMarksError(Exception):
    pass

try:

    marks = int(input("Enter Marks: "))

    if marks > 100 or marks < 0:
        raise InvalidMarksError("Marks must be between 0 and 100.")

    print("Valid Marks")

except InvalidMarksError as error:

    print(error)

print()

# ==========================================================
# 12. Common Python Exceptions
# ==========================================================

print("========== Common Python Exceptions ==========")

print("1. ZeroDivisionError")
print("2. ValueError")
print("3. TypeError")
print("4. IndexError")
print("5. KeyError")
print("6. FileNotFoundError")

print()

# ==========================================================
# Examples of Common Exceptions
# ==========================================================

print("========== ZeroDivisionError ==========")

try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero.")

print()

print("========== ValueError ==========")

try:
    number = int("Python")

except ValueError:
    print("Invalid integer value.")

print()

print("========== TypeError ==========")

try:
    result = "10" + 5

except TypeError:
    print("Different data types cannot be added.")

print()

print("========== IndexError ==========")

try:

    numbers = [10, 20, 30]

    print(numbers[10])

except IndexError:
    print("List index out of range.")

print()

print("========== KeyError ==========")

try:

    student = {"Name": "Ali"}

    print(student["Age"])

except KeyError:
    print("Key not found.")

print()

print("========== FileNotFoundError ==========")

try:

    file = open("student.txt", "r")

except FileNotFoundError:
    print("File does not exist.")

print()

# ==========================================================
# Program 1: Division Calculator
# ==========================================================

print("========== Division Calculator ==========")

try:

    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:

    print("Error: Cannot divide by zero.")

except ValueError:

    print("Error: Please enter valid integers.")

print()

# ==========================================================
# Program 2: Integer Input Validation
# ==========================================================

print("========== Integer Input Validation ==========")

try:

    number = int(input("Enter an Integer: "))

    print("You Entered:", number)

except ValueError:

    print("Error: Only integers are allowed.")

print()

# ==========================================================
# Program 3: Password Validation
# ==========================================================

print("========== Password Validation ==========")

true_password = "Python123"

for attempt in range(3):

    try:

        password = input("Enter Password: ")

        if password == true_password:

            print("Welcome!")
            break

        else:

            print("Wrong Password")

    except Exception as error:

        print("Error:", error)

else:

    print("Too many attempts. Access Blocked!")

print()

# ==========================================================
# Program 4: ATM Login System
# ==========================================================

print("========== ATM Login ==========")

true_username = "esha"
true_password = 1245
balance = 1000

try:

    username = input("Enter Username: ")
    password = int(input("Enter Password: "))

    if username == true_username and password == true_password:

        print("Login Successful")
        print("Available Balance =", balance)

    else:

        print("Invalid Username or Password")

except ValueError:

    print("Password must be an integer.")

print()