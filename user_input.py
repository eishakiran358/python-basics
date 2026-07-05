
# ==========================================================
# Python User Input
# ==========================================================


# ==========================================================
# 1. Basic User Input
# ==========================================================

print("========== Basic User Input ==========")

name = input("Enter your name: ")
print("Hello,", name)

print()


# ==========================================================
# 2. Input Always Returns a String
# ==========================================================

print("========== Input Always Returns String ==========")

age = input("Enter your age: ")

print("Value:", age)
print("Data Type:", type(age))

print()


# ==========================================================
# 3. Type Casting to Integer
# ==========================================================

print("========== Integer Input ==========")

age = int(input("Enter your age: "))

print("Age:", age)
print("Data Type:", type(age))

print()


# ==========================================================
# 4. Type Casting to Float
# ==========================================================

print("========== Float Input ==========")

height = float(input("Enter your height in feet: "))

print("Height:", height)
print("Data Type:", type(height))

print()


# ==========================================================
# 5. String Input
# ==========================================================

print("========== String Input ==========")

city = str(input("Enter your city: "))

print("City:", city)
print("Data Type:", type(city))

print()


# ==========================================================
# 6. Multiple Inputs
# ==========================================================

print("========== Multiple Inputs ==========")

first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")

print("Full Name:", first_name, last_name)

print()


# ==========================================================
# 7. Taking Two Numbers from User
# ==========================================================

print("========== Two Numbers ==========")

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("First Number:", num1)
print("Second Number:", num2)

print()


# ==========================================================
# 8. Addition Using User Input
# ==========================================================

print("========== Addition Calculator ==========")

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

result = num1 + num2

print("Addition =", result)

print()


# ==========================================================
# 9. Student Information Example
# ==========================================================

print("========== Student Information ==========")

student_name = input("Enter Student Name: ")
student_age = int(input("Enter Student Age: "))
student_marks = float(input("Enter Student Marks: "))

print("\nStudent Details")
print("Name :", student_name)
print("Age  :", student_age)
print("Marks:", student_marks)

print()


# ==========================================================
# 10. Using f-Strings with User Input
# ==========================================================

print("========== f-String Example ==========")

name = input("Enter Your Name: ")
profession = input("Enter Your Profession: ")

print(f"My name is {name} and I am a {profession}.")

print()


# ==========================================================
# 11. Boolean Input Example
# ==========================================================

print("========== Boolean Example ==========")

value = bool(input("Enter Any Value: "))

print("Boolean Value:", value)
print("Data Type:", type(value))

print()


print("\n===== Square Calculator =====")

number = int(input("Enter a number: "))
print("Square is:", number ** 2)

# ==========================================
#  Area of Rectangle
# ==========================================

length = float(input("Length: "))
width = float(input("Width: "))

area = length * width

print("Area =", area)

# ==========================================
# Mini Exercise - Average
# ==========================================

n1 = float(input("Number 1: "))
n2 = float(input("Number 2: "))
n3 = float(input("Number 3: "))

average = (n1 + n2 + n3) / 3

print("Average =", average)
