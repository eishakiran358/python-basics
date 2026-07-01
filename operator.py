# ==========================================================
# Python Operators
# ==========================================================


# ==========================================================
# 1. Arithmetic Operators
# ==========================================================

print("========== Arithmetic Operators ==========")

a = 15
b = 4

print("a =", a)
print("b =", b)

print("Addition (+):", a + b)
print("Subtraction (-):", a - b)
print("Multiplication (*):", a * b)
print("Division (/):", a / b)
print("Floor Division (//):", a // b)
print("Modulus (%):", a % b)
print("Exponent (**):", a ** b)

print()


# ==========================================================
# 2. Assignment Operators
# ==========================================================

print("========== Assignment Operators ==========")

x = 10
print("Initial Value:", x)

x += 5
print("x += 5 :", x)

x -= 2
print("x -= 2 :", x)

x *= 3
print("x *= 3 :", x)

x /= 2
print("x /= 2 :", x)

x //= 2
print("x //= 2 :", x)

x %= 4
print("x %= 4 :", x)

x **= 2
print("x **= 2 :", x)

print()


# ==========================================================
# 3. Comparison Operators
# ==========================================================

print("========== Comparison Operators ==========")

a = 20
b = 10

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b :", a > b)
print("a < b :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

print()


# ==========================================================
# 4. Logical Operators
# ==========================================================

print("========== Logical Operators ==========")

x = True
y = False

print("x and y :", x and y)
print("x or y :", x or y)
print("not x :", not x)

print()

##==========================================
#QUIZ
#===========================================

# Simple Calculator

print("===== Calculator =====")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Division")
print("5. Exit")

while True:

    SELECT = int(input("\nChoose an option: "))

    if SELECT == 5:
        print("Calculator Closed.")
        break

    if SELECT in [1, 2, 3, 4]:

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        def add():
            result = num1 + num2
            print("Addition =", result)

        def subtract():
            result = num1 - num2
            print("Subtraction =", result)

        def multiply():
            result = num1 * num2
            print("Multiplication =", result)

        def division():
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print("Division =", result)

        if SELECT == 1:
            add()

        elif SELECT == 2:
            subtract()

        elif SELECT == 3:
            multiply()

        elif SELECT == 4:
            division()

    else:
        print("Invalid Choice! Please select between 1 and 5.")