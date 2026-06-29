#         ............ Variables ..........
# A variable is a container that stores data or values in memory.
# A variable is a named location in memory used to store data values.

name = "Eishaa"
age = 21
cgpa = 3.54
student = True

#     .............  Vaiable datatypes..........

# 1.String (str):
# A string is a sequence of characters enclosed within single (' ') or double (" ") quotation marks.
name = "Eishaa"
city = "MULTAN"
message = "Welcome to Python"

print("String Examples:")
print("Name:", name)
print("City:", city)
print("Message:", message)

# 2. Integer (int):
# An integer is a whole number without a decimal point.
age = 21
marks = 95
year = 2026

print("Integer Examples:")
print("Age:", age)
print("Marks:", marks)
print("Year:", year)

# 3. Float (float):
# A float is a number that contains a decimal point.
temperature = 36.5
price = 999.99
print("Float Examples:")
print("CGPA:", cgpa)
print("Temperature:", temperature)
print("Price:", price)

# 4. Boolean (bool):
# A boolean data type represents one of two values: True or False.
student = True
has_passed = True
is_married = False
print("Boolean Examples:")
print(" Student:", student)
print("Has Passed:", has_passed)
print("Is Married:", is_married)


# Displaying values
print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)
print("Student Status:", student)

# Updating a variable
print("Updating Age...")
age = 22
print("New Age:", age)

# Multiple variables
city, country = "Karachi", "Pakistan"

print("City:", city)
print("Country:", country)

#   Single or Double Quotes 

# In Python, a string is a sequence of characters (text). You can create a string by
#  using either single quotes (' ') or double quotes (" ").

# Both work in exactly the same way.
name = 'Eishaa'
print(name)
# Using Double Quotes
name = "Eishaa"
print(name)

#..................Variable Names.............
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

# Rules for Python variables:

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

#valid example
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#..................naming cases (styles) .................
# we use variables with more than one word, we follow different naming cases (styles). The most common cases are:

#  1. Snake Case ()
# All words are lowercase.
# Words are separated by underscores (_).

student_name = "Ali"
total_marks = 90
user_age = 20

# 2. Camel Case
# The first word starts with a lowercase letter.
# Each next word starts with a capital letter.

studentName = "Ali"
totalMarks = 90
userAge = 20

# 3. Pascal Case
# Every word starts with a capital letter.

StudentName = "Ali"
TotalMarks = 90
UserAge = 20

# 4. UPPER_CASE (Constants)
# All letters are uppercase.
# Words are separated by underscores.
# Usually used for constants.

PI = 3.14
MAX_SIZE = 100
DATABASE_NAME = "school"

# 5.Flat Case
# All letters are lowercase.
# No spaces are used.
# No underscores (_) are used.

myname = "Ali"
studentage = 20
totalmarks = 90

#example
myName= "eisha"   #camelcase First word small, next words capital
print(myName)
myname="allsmall" #flat case    lowercase no space no underscores
MyName="Allsmall" #pascal case   Each word starts with an uppercase lette
my_name="allsmall" #smakecase   #All letters are lowercase, and words are separated by underscores