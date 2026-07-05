# ==========================================================
# Python While Loop

# 1. What is While Loop?
# ==========================================================

"""
Definition:
A while loop repeatedly executes a block of code
as long as the given condition is True.

Syntax:

while condition:
    # Code
"""

# ==========================================================
# 2. Print Numbers (1 to 10)
# ==========================================================

print("========== Print Numbers (1 to 10) ==========")

i = 1

while i <= 10:
    print(i)
    i += 1

print()

# ==========================================================
# 3. Reverse Counting (10 to 1)
# ==========================================================

print("========== Reverse Counting ==========")

i = 10

while i >= 1:
    print(i)
    i -= 1

print()

# ==========================================================
# 4. Print Even Numbers (1 to 50)
# ==========================================================

print("========== Even Numbers ==========")

i = 1

while i <= 50:

    if i % 2 == 0:
        print(i)

    i += 1

print()

# ==========================================================
# 5. Print Odd Numbers (1 to 50)
# ==========================================================

print("========== Odd Numbers ==========")

i = 1

while i <= 50:

    if i % 2 != 0:
        print(i)

    i += 1

print()

# ==========================================================
# 6. Sum of Numbers (1 to 100)
# ==========================================================

print("========== Sum of Numbers ==========")

i = 1
total = 0

while i <= 100:

    total += i
    i += 1

print("Sum =", total)

print()

# ==========================================================
# 7. Multiplication Table (Any Number)
# ==========================================================

print("========== Multiplication Table ==========")

number = int(input("Enter a Number: "))

i = 1

while i <= 10:

    print(f"{number} x {i} = {number * i}")

    i += 1

print()

# ==========================================================
# 8. Infinite Loop (Explanation)
# ==========================================================

print("========== Infinite Loop ==========")

"""
Definition:
An Infinite Loop is a loop that never ends because
its condition always remains True.

Example:

while True:
    print("Hello")

(Do not run this code unless you use break.)
"""

print()

# ==========================================================
# 9. break Statement
# ==========================================================

print("========== break Statement ==========")

i = 1

while i <= 10:

    if i == 6:
        break

    print(i)

    i += 1

print()

# ==========================================================
# 10. continue Statement
# ==========================================================

print("========== continue Statement ==========")

i = 0

while i < 10:

    i += 1

    if i == 5:
        continue

    print(i)

print()

# ==========================================================
# 11. else with while Loop
# ==========================================================

print("========== else with while Loop ==========")

i = 1

while i <= 5:

    print(i)

    i += 1

else:
    print("Loop Completed Successfully.")

print()

# ==========================================================
# 12. pass Statement
# ==========================================================

print("========== pass Statement ==========")

i = 1

while i <= 5:

    if i == 3:
        pass

    print(i)

    i += 1

print()

# ==========================================================
# 13. Password Checker
# ==========================================================

print("========== Password Checker ==========")

"""
Definition:
The program keeps asking for a password
until the correct password is entered.
"""

password = "eisha123"

while True:

    entered_password = input("Enter Password: ")

    if entered_password == password:
        print("Login Successful!")
        break

    else:
        print("Incorrect Password. Try Again!")

print()


# ==========================================================
# 14. Login System
# ==========================================================

print("========== Login System ==========")

"""
Definition:
The user enters a username and password.
The loop continues until the correct credentials
are entered.
"""

username = "eisha"
password = "12345"

while True:

    user = input("Username: ")
    pwd = input("Password: ")

    if user == username and pwd == password:
        print("Welcome,", user)
        break

    else:
        print("Invalid Username or Password!")

print()


# ==========================================================
# 15. ATM Machine
# ==========================================================

print("========== ATM Machine ==========")

"""
Definition:
A simple ATM menu using a while loop.
"""

balance = 10000

while True:

    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":

        print("Current Balance =", balance)

    elif choice == "2":

        amount = float(input("Enter Deposit Amount: "))
        balance += amount
        print("Updated Balance =", balance)

    elif choice == "3":

        amount = float(input("Enter Withdraw Amount: "))

        if amount <= balance:
            balance -= amount
            print("Remaining Balance =", balance)

        else:
            print("Insufficient Balance!")

    elif choice == "4":

        print("Thank You for Using the ATM.")
        break

    else:
        print("Invalid Choice!")

print()


# ==========================================================
# 16. Menu Driven Calculator
# ==========================================================

print("========== Menu Driven Calculator ==========")

"""
Definition:
A calculator that repeatedly performs operations
until the user chooses to exit.
"""

while True:

    print("\n===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Choose an Option: ")

    if choice == "5":
        print("Calculator Closed.")
        break

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    if choice == "1":
        print("Answer =", num1 + num2)

    elif choice == "2":
        print("Answer =", num1 - num2)

    elif choice == "3":
        print("Answer =", num1 * num2)

    elif choice == "4":

        if num2 != 0:
            print("Answer =", num1 / num2)

        else:
            print("Cannot Divide by Zero!")

    else:
        print("Invalid Choice!")

print()


# ==========================================================
# 17. Student Result System
# ==========================================================

print("========== Student Result System ==========")

"""
Definition:
Calculates total marks, percentage,
grade, and pass/fail status.
"""

while True:

    name = input("Student Name: ")

    marks = []

    for i in range(1, 6):
        mark = float(input(f"Subject {i} Marks: "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
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
    print("Student:", name)
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)

    again = input("\nCheck another result? (yes/no): ").lower()

    if again != "yes":
        break

print()


# ==========================================================
# 18. Number Analyzer
# ==========================================================

print("========== Number Analyzer ==========")

"""
Definition:
Checks whether a number is
Even/Odd and Positive/Negative.
"""

while True:

    number = int(input("Enter a Number: "))

    if number % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

    if number > 0:
        print("Positive Number")
    elif number < 0:
        print("Negative Number")
    else:
        print("Zero")

    choice = input("Analyze Another Number? (yes/no): ").lower()

    if choice != "yes":
        break

print()


# ==========================================================
# 19. Countdown Timer
# ==========================================================

print("========== Countdown Timer ==========")

"""
Definition:
Counts down from a user-entered number to zero.
"""

count = int(input("Enter Starting Number: "))

while count >= 0:

    print(count)
    count -= 1

print("Time's Up!")

print()


# ==========================================================
# 20. Guess Number Game
# ==========================================================

print("========== Guess Number Game ==========")

"""
Definition:
The user keeps guessing until
the correct number is entered.
"""

secret_number = 7

while True:

    guess = int(input("Guess the Number (1-10): "))

    if guess == secret_number:
        print("Congratulations! Correct Guess.")
        break

    elif guess < secret_number:
        print("Too Low!")

    else:
        print("Too High!")

print()

