# ==========================================================
# 1. What is Polymorphism?
# ==========================================================

"""
Definition

Polymorphism is one of the four pillars of
Object-Oriented Programming (OOP).

The word Polymorphism comes from two Greek words:

Poly  = Many
Morph = Forms

Polymorphism means:

"One Thing, Many Forms."

In Python, Polymorphism allows the same method,
function, or operator to perform different actions
depending on the object.

Simple Definition

One Method
Different Objects
Different Behaviors
"""

# ==========================================================
# Example
# ==========================================================

"""
Suppose we have different animals.

Dog  -> sound() -> Bark

Cat  -> sound() -> Meow

Cow  -> sound() -> Moo

The method name is the same.

sound()

But every object performs a different action.

This is called Polymorphism.
"""

# ==========================================================
# 2. Why Use Polymorphism?
# ==========================================================

"""
Why Use Polymorphism?

✔ Makes code reusable.

✔ Reduces duplicate code.

✔ Makes programs easier to maintain.

✔ Makes code flexible.

✔ Easy to extend programs.

✔ Helps write professional OOP code.
"""

# ==========================================================
# 3. Advantages of Polymorphism
# ==========================================================

"""
Advantages

1. Code Reusability

2. Flexibility

3. Easy Maintenance

4. Better Readability

5. Less Code Duplication

6. Easy to Extend

7. Supports Runtime Decisions

8. Professional Programming
"""

# ==========================================================
# 4. Method Overriding (Runtime Polymorphism)
# ==========================================================

"""
Method Overriding

Method Overriding happens when a child class
creates its own version of a method that already
exists in the parent class.

The method name remains the same,
but the implementation changes.

This is called Runtime Polymorphism.
"""

print("========== Method Overriding ==========\n")


# Parent Class

class Animal:

    def sound(self):

        print("Animal makes a sound.")


# Child Class

class Dog(Animal):

    # Override Parent Method
    def sound(self):

        print("Dog says: Bark Bark")


# Child Class

class Cat(Animal):

    # Override Parent Method
    def sound(self):

        print("Cat says: Meow Meow")


# Objects

dog = Dog()

cat = Cat()

dog.sound()

cat.sound()

print()

# ==========================================================
# Explanation
# ==========================================================

"""
Animal class contains

sound()

Dog class overrides

sound()

Cat class also overrides

sound()

Same Method

Different Output

This is Runtime Polymorphism.
"""

# ==========================================================
# 5. Operator Overloading (Introduction)
# ==========================================================

"""
Operator Overloading

Operator Overloading means
using the same operator for
different purposes.

Example

+

Integer

5 + 10

Output

15

String

"Hello" + " World"

Output

Hello World

List

[1,2] + [3,4]

Output

[1,2,3,4]

Same Operator

Different Behaviors

This is also Polymorphism.
"""

print("========== Operator Overloading ==========\n")

print(10 + 20)

print("Python " + "Programming")

print([1, 2] + [3, 4])

print()

# ==========================================================
# 6. Simple Polymorphism Example
# ==========================================================

"""
Simple Example

Different objects

Same Method

Different Output
"""

print("========== Simple Polymorphism Example ==========\n")


class Bird:

    def fly(self):

        print("Bird is Flying")


class Airplane:

    def fly(self):

        print("Airplane is Flying")


class Drone:

    def fly(self):

        print("Drone is Flying")


# Create Objects

bird = Bird()

plane = Airplane()

drone = Drone()

# Store Objects in a List

objects = [

    bird,

    plane,

    drone

]

# Same Method

for obj in objects:

    obj.fly()

print()
#===============================================
# PROBLEM
#===============================================
# Parent Class
class Animal:

    # Parent method
    def sound(self):
        pass


# Child Class
class Dog(Animal):   # Animal class ko inherit kiya

    # Parent method ko override kiya
    def sound(self):
        print("Dog says Bark")


# Child Class
class Cat(Animal):   # Animal class ko inherit kiya

    # Parent method ko override kiya
    def sound(self):
        print("Cat says Meow")


# Object banaya
dog = Dog()

# Object banaya
cat = Cat()

# Parent reference ki list banai
animals = [dog, cat]

# Har object ka same method call hoga
for animal in animals:

    # Runtime par decide hoga konsa sound() chalega
    animal.sound()

# ==========================================================
# Project  : Shape Area Calculator
# ==========================================================

"""
Problem Statement

Create a Shape System using Polymorphism.

Requirements

1. Create a Parent Class (Shape)
2. Create Rectangle, Circle and Triangle classes
3. Override area() and perimeter() methods
4. Use Polymorphism to calculate Area and Perimeter
"""

# Import math module for Circle and Triangle calculations
import math


# ==========================================================
# Parent Class
# ==========================================================

class Shape:

    # Parent method
    def area(self):
        pass

    # Parent method
    def perimeter(self):
        pass


# ==========================================================
# Child Class : Rectangle
# ==========================================================

class Rectangle(Shape):     # Inherit Shape class

    # Constructor
    def __init__(self, length, width):

        # Object attributes
        self.length = length
        self.width = width

    # Override Parent Method
    def area(self):

        return self.length * self.width

    # Override Parent Method
    def perimeter(self):

        return 2 * (self.length + self.width)


# ==========================================================
# Child Class : Circle
# ==========================================================

class Circle(Shape):        # Inherit Shape class

    # Constructor
    def __init__(self, radius):

        self.radius = radius

    # Override Parent Method
    def area(self):

        return math.pi * self.radius ** 2

    # Override Parent Method
    def perimeter(self):

        return 2 * math.pi * self.radius


# ==========================================================
# Child Class : Triangle
# ==========================================================

class Triangle(Shape):      # Inherit Shape class

    # Constructor
    def __init__(self, side1, side2, side3):

        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    # Override Parent Method
    def area(self):

        # Heron's Formula
        s = (self.side1 + self.side2 + self.side3) / 2

        return math.sqrt(
            s *
            (s - self.side1) *
            (s - self.side2) *
            (s - self.side3)
        )

    # Override Parent Method
    def perimeter(self):

        return self.side1 + self.side2 + self.side3


# ==========================================================
# Objects
# ==========================================================

# Rectangle Object
rectangle = Rectangle(10, 5)

# Circle Object
circle = Circle(7)

# Triangle Object
triangle = Triangle(3, 4, 5)


# ==========================================================
# Store Objects in List
# ==========================================================

# Different objects stored in one list
shapes = [

    rectangle,

    circle,

    triangle

]
# ==========================================================
# Polymorphism
# ==========================================================

# Variable to store total area
total_area = 0

# Loop through all objects
for shape in shapes:

    # Same method
    # Different output depending on object
    print("Area :", round(shape.area(), 2))

    # Same method
    print("Perimeter :", round(shape.perimeter(), 2))

    print("-" * 30)

    # Add area
    total_area += shape.area()


# Display Total Area
print("Total Area :", round(total_area, 2))

# ==========================================================
# Project : Payment System
# ==========================================================

"""
Problem Statement

Create a Payment System using Polymorphism.

Requirements

1. Create a Parent Class (Payment)

2. Create three Child Classes:
   - CreditCard
   - PayPal
   - Cash

3. Each class should override the pay() method.

4. Use Polymorphism to process payments.
"""

# ==========================================================
# Parent Class
# ==========================================================

class Payment:

    # Parent Method
    def pay(self, amount):

        # pass means method will be implemented
        # in child classes
        pass


# ==========================================================
# Child Class : Credit Card
# ==========================================================

class CreditCard(Payment):      # Inherit Parent Class

    # Override Parent Method
    def pay(self, amount):

        print(f"Paid Rs.{amount} using Credit Card.")


# ==========================================================
# Child Class : PayPal
# ==========================================================

class PayPal(Payment):          # Inherit Parent Class

    # Override Parent Method
    def pay(self, amount):

        print(f"Paid Rs.{amount} using PayPal.")


# ==========================================================
# Child Class : Cash
# ==========================================================

class Cash(Payment):            # Inherit Parent Class

    # Override Parent Method
    def pay(self, amount):

        print(f"Paid Rs.{amount} using Cash.")


# ==========================================================
# Function
# ==========================================================

# This function accepts any Payment object
def process_payment(payment_method, amount):

    # Same method call
    # Runtime decides which class method executes
    payment_method.pay(amount)


# ==========================================================
# Create Objects
# ==========================================================

# Credit Card Object
card = CreditCard()

# PayPal Object
paypal = PayPal()

# Cash Object
cash = Cash()


# ==========================================================
# Polymorphism
# ==========================================================

# Same function

# Different Objects

# Different Outputs

process_payment(card, 5000)

process_payment(paypal, 2500)

process_payment(cash, 1000)