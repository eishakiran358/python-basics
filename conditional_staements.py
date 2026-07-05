# ==========================================================
# Python Conditional Statements
# ==========================================================

print("========== Python Conditional Statements ==========\n")

# ==========================================================
# 1. What is a Conditional Statement?
# ==========================================================

print("========== 1. if Statement ==========")

age = 20

if age >= 18:
    print("You are eligible to vote.")

print()

# ==========================================================
# 2. if Statement
# ==========================================================

print("========== 2. if Statement ==========")

number = 15

if number > 10:
    print("Number is greater than 10.")

print()

# ==========================================================
# 3. if-else Statement
# ==========================================================

print("========== 3. if-else Statement ==========")

number = int(input("Enter a Number: "))

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")

print()

# ==========================================================
# 4. Positive, Negative or Zero
# ==========================================================

print("========== 4. Positive / Negative / Zero ==========")

num = int(input("Enter a Number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

print()

# ==========================================================
# 5. if-elif-else Statement
# ==========================================================

print("========== 5. Grade Calculator ==========")

marks = int(input("Enter Your Marks: "))

if marks >= 90:
    print("Grade A+")

elif marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 50:
    print("Grade D")

else:
    print("Fail")

print()

# ==========================================================
# 6. Nested if Statement
# ==========================================================

print("========== 6. Nested if ==========")

age = int(input("Enter Your Age: "))

if age >= 18:

    nationality = input("Are you Pakistani? (yes/no): ").lower()

    if nationality == "yes":
        print("Eligible to Vote")
    else:
        print("Nationality Required")

else:
    print("Not Eligible")

print()

# ==========================================================
# 7. Comparison Operators
# ==========================================================

print("========== 7. Comparison Operators ==========")

a = 10
b = 20

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

print()

# ==========================================================
# 8. Logical Operators
# ==========================================================

print("========== 8. Logical Operators ==========")

age = int(input("Enter Age: "))
citizen = input("Are you Pakistani? (yes/no): ").lower()

if age >= 18 and citizen == "yes":
    print("Eligible to Vote")
else:
    print("Not Eligible")

print()

# OR Operator

username = input("Username: ")

if username == "admin" or username == "teacher":
    print("Access Granted")
else:
    print("Access Denied")

print()

# NOT Operator

logged_in = False

if not logged_in:
    print("Please Login")

print()

# ==========================================================
# 9. Membership Operators
# ==========================================================

print("========== 9. Membership Operators ==========")

fruits = ["Apple", "Banana", "Mango"]

fruit = input("Enter Fruit Name: ")

if fruit in fruits:
    print("Fruit Found")
else:
    print("Fruit Not Found")

print()

# ==========================================================
# 10. Identity Operators
# ==========================================================

print("========== 10. Identity Operators ==========")

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("x is y :", x is y)
print("x is z :", x is z)
print("x == z :", x == z)

print()

# ==========================================================
# 11. Ternary Operator
# ==========================================================

print("========== 11. Ternary Operator ==========")

age = int(input("Enter Age: "))

message = "Adult" if age >= 18 else "Minor"

print(message)

print()

# ==========================================================
# 12. Multiple Conditions Example
# ==========================================================

print("========== 12. Multiple Conditions ==========")

salary = int(input("Enter Salary: "))
experience = int(input("Enter Experience (Years): "))

if salary >= 50000 and experience >= 2:
    print("Eligible for Promotion")
else:
    print("Not Eligible")

print()

# 13. Largest of Two Numbers
# ==========================================================

print("========== Largest of Two Numbers ==========")

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

if num1 > num2:
    print(num1, "is Greater")
else:
    print(num2, "is Greater")

print()

# ==========================================================
# 14. Largest of Three Numbers
# ==========================================================

print("========== Largest of Three Numbers ==========")

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a >= b and a >= c:
    print("Largest Number =", a)

elif b >= a and b >= c:
    print("Largest Number =", b)

else:
    print("Largest Number =", c)

print()

# ==========================================================
# 15. Leap Year Checker
# ==========================================================

print("========== Leap Year Checker ==========")

year = int(input("Enter Year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")

print()

# ==========================================================
# 16. Simple Calculator
# ==========================================================

print("========== Simple Calculator ==========")

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Choose Operation (1-4): ")

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
        print("Cannot Divide by Zero")

else:
    print("Invalid Choice")

print()

# ==========================================================
# 17. Password Checker
# ==========================================================

print("========== Password Checker ==========")

password = input("Enter Password: ")

if password == "admin123":
    print("Login Successful")
else:
    print("Wrong Password")

print()

# ==========================================================
# 18. Login System
# ==========================================================

print("========== Login System ==========")

username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "12345":
    print("Welcome Admin")

else:
    print("Invalid Username or Password")

print()

# ==========================================================
# 19. ATM Menu
# ==========================================================

print("========== ATM Menu ==========")

balance = 10000

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")

option = input("Choose Option: ")

if option == "1":

    print("Balance =", balance)

elif option == "2":

    amount = float(input("Deposit Amount: "))
    balance += amount
    print("Updated Balance =", balance)

elif option == "3":

    amount = float(input("Withdraw Amount: "))

    if amount <= balance:
        balance -= amount
        print("Remaining Balance =", balance)

    else:
        print("Insufficient Balance")

else:
    print("Invalid Option")

print()

# ==========================================================
# 20. Age Category
# ==========================================================

print("========== Age Category ==========")

age = int(input("Enter Age: "))

if age < 13:
    print("Child")

elif age < 20:
    print("Teenager")

elif age < 60:
    print("Adult")

else:
    print("Senior Citizen")

print()

# ==========================================================
# 21. BMI Checker
# ==========================================================

print("========== BMI Checker ==========")

weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

bmi = weight / (height ** 2)

print("BMI =", round(bmi, 2))

if bmi < 18.5:
    print("Underweight")

elif bmi < 25:
    print("Normal Weight")

elif bmi < 30:
    print("Overweight")

else:
    print("Obese")

print()