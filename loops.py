
# ==========================================================
# Python For Loop
# ==========================================================

print("========== Python For Loop ==========\n")

# ==========================================================
# 1. Print Numbers (1 to 10)
# ==========================================================

print("========== Print Numbers (1 to 10) ==========")

for i in range(1, 11):
    print(i)

print()

# ==========================================================
# 2. range(stop)
# ==========================================================

print("========== range(stop) ==========")

for i in range(5):
    print(i)

print()

# ==========================================================
# 3. range(start, stop)
# ==========================================================

print("========== range(start, stop) ==========")

for i in range(5, 11):
    print(i)

print()

# ==========================================================
# 4. range(start, stop, step)
# ==========================================================

print("========== range(start, stop, step) ==========")

for i in range(0, 21, 2):
    print(i)

print()

# ==========================================================
# 5. Reverse Counting
# ==========================================================

print("========== Reverse Counting ==========")

for i in range(10, 0, -1):
    print(i)

print()

# ==========================================================
# 6. Loop Through a String
# ==========================================================

print("========== Loop Through String ==========")

text = "Python"

for letter in text:
    print(letter)

print()

# ==========================================================
# 7. Loop Through a List
# ==========================================================

print("========== Loop Through List ==========")

fruits = ["Apple", "Banana", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)

print()

# ==========================================================
# 8. Print Table of 5
# ==========================================================

print("========== Table of 5 ==========")

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

print()

# ==========================================================
# 9. User Input Table
# ==========================================================

print("========== User Input Table ==========")

number = int(input("Enter a Number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print()

# ==========================================================
# 10. Sum of Numbers (1 to 100)
# ==========================================================

print("========== Sum of Numbers ==========")

total = 0

for i in range(1, 101):
    total += i

print("Sum =", total)

print()

# ==========================================================
# 11. Print Even Numbers (1 to 50)
# ==========================================================

print("========== Even Numbers ==========")

for i in range(1, 51):

    if i % 2 == 0:
        print(i)

print()

# ==========================================================
# 12. Print Odd Numbers (1 to 50)
# ==========================================================

print("========== Odd Numbers ==========")

for i in range(1, 51):

    if i % 2 != 0:
        print(i)

print()

# ==========================================================
# 13. break Statement
# ==========================================================

print("========== break Statement ==========")

for i in range(1, 11):

    if i == 6:
        break

    print(i)

print()

# ==========================================================
# 14. continue Statement
# ==========================================================

print("========== continue Statement ==========")

for i in range(1, 11):

    if i == 5:
        continue

    print(i)

print()

# ==========================================================
# 15. else with for Loop
# ==========================================================

print("========== else with for Loop ==========")

for i in range(1, 6):
    print(i)

else:
    print("Loop Completed Successfully.")

print()

# ==========================================================
# 16. pass Statement
# ==========================================================

print("========== pass Statement ==========")

for i in range(5):

    if i == 3:
        pass

    print(i)

print()

# ==========================================================
# 17. Nested For Loop
# ==========================================================

print("========== Nested For Loop ==========")

"""
Definition:
A Nested For Loop is a loop inside another loop.
It is commonly used for pattern printing, matrices,
and row-column operations.
"""

for row in range(1, 4):

    for column in range(1, 4):
        print(f"({row},{column})", end=" ")

    print()

print()


# ==========================================================
# 18. Multiplication Table (Any Number)
# ==========================================================

print("========== Multiplication Table ==========")

"""
Definition:
This program prints the multiplication table
of any number entered by the user.
"""

number = int(input("Enter a Number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print()


# ==========================================================
# 19. Factorial
# ==========================================================

print("========== Factorial ==========")

"""
Definition:
Factorial is the product of all positive integers
from 1 to a given number.

Example:
5! = 5 × 4 × 3 × 2 × 1 = 120
"""

number = int(input("Enter a Number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial =", factorial)

print()


# ==========================================================
# 20. Prime Number
# ==========================================================

print("========== Prime Number ==========")

"""
Definition:
A Prime Number has exactly two factors:
1 and itself.

Examples:
2, 3, 5, 7, 11
"""

number = int(input("Enter a Number: "))

count = 0

for i in range(1, number + 1):

    if number % i == 0:
        count += 1

if count == 2:
    print(number, "is a Prime Number")

else:
    print(number, "is Not a Prime Number")

print()


# ==========================================================
# 21. Palindrome Number
# ==========================================================

print("========== Palindrome Number ==========")

"""
Definition:
A Palindrome Number reads the same
forward and backward.

Examples:
121
1331
1221
"""

number = input("Enter a Number: ")

if number == number[::-1]:
    print(number, "is a Palindrome")

else:
    print(number, "is Not a Palindrome")

print()


# ==========================================================
# 22. Armstrong Number
# ==========================================================

print("========== Armstrong Number ==========")

"""
Definition:
An Armstrong Number is a number equal to
the sum of its own digits raised to the power
of the number of digits.

Example:
153

1³ + 5³ + 3³ = 153
"""

number = int(input("Enter a Number: "))

power = len(str(number))

total = 0

temp = number

while temp > 0:

    digit = temp % 10
    total += digit ** power
    temp //= 10

if total == number:
    print(number, "is an Armstrong Number")

else:
    print(number, "is Not an Armstrong Number")

print()

# ==========================================================
# 23. Number Pattern
# ==========================================================

print("========== Number Pattern ==========")

"""
Definition:
A Number Pattern prints numbers in a specific
sequence using nested for loops.
"""

rows = int(input("Enter Number of Rows: "))

for i in range(1, rows + 1):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()

print()


# ==========================================================
# 24. Student Result System
# ==========================================================

print("========== Student Result System ==========")

"""
Definition:
This mini project calculates total marks,
percentage, grade, and pass/fail status.
"""

name = input("Enter Student Name: ")

sub1 = float(input("Subject 1 Marks: "))
sub2 = float(input("Subject 2 Marks: "))
sub3 = float(input("Subject 3 Marks: "))
sub4 = float(input("Subject 4 Marks: "))
sub5 = float(input("Subject 5 Marks: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

print("\n========== Result ==========")
print("Student Name :", name)
print("Total Marks  :", total)
print("Percentage   :", percentage)

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

print("Grade        :", grade)

print()


# ==========================================================
# 25. Table Generator
# ==========================================================

print("========== Table Generator ==========")

"""
Definition:
Print multiplication tables from
1 to any number.
"""

limit = int(input("Print Tables Up To: "))

for table in range(1, limit + 1):

    print(f"\nTable of {table}")

    for i in range(1, 11):
        print(f"{table} x {i} = {table*i}")

print()


# ==========================================================
# 26. Number Analyzer
# ==========================================================

print("========== Number Analyzer ==========")

"""
Definition:
Checks whether a number is
Even/Odd
Positive/Negative
Prime or Not
"""

number = int(input("Enter a Number: "))

# Even / Odd
if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Positive / Negative
if number > 0:
    print("Positive Number")

elif number < 0:
    print("Negative Number")

else:
    print("Zero")

# Prime
count = 0

for i in range(1, number + 1):

    if number % i == 0:
        count += 1

if count == 2:
    print("Prime Number")

else:
    print("Not Prime Number")

print()


# ==========================================================
# 27. Pattern Generator
# ==========================================================

print("========== Pattern Generator ==========")

"""
Definition:
Generate different star patterns
using nested for loops.
"""

rows = int(input("Enter Number of Rows: "))

print("\nSquare Pattern")

for i in range(rows):

    for j in range(rows):
        print("*", end=" ")

    print()

print("\nRight Triangle")

for i in range(1, rows + 1):

    for j in range(i):
        print("*", end=" ")

    print()

print("\nNumber Pattern")

for i in range(1, rows + 1):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()

print()


      
      
      