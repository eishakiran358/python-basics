# ┌─────────────────────────────────────────────────────────┐
# │                    ABSTRACTION                           │
# │                                                          │
# │   "Hide implementation details, show only functionality"│
# │                                                          │
# │   ┌─────────────────────────────────────────────────┐   │
# │   │              CAR (Abstract View)                 │   │
# │   │  ┌─────────────────────────────────────────┐    │   │
# │   │  │  WHAT YOU SEE (Public Interface)        │    │   │
# │   │  │  • Steering wheel                       │    │   │
# │   │  │  • Pedals (accelerator, brake)          │    │   │
# │   │  │  • Gear shift                           │    │   │
# │   │  │  • Dashboard                            │    │   │
# │   │  └─────────────────────────────────────────┘    │   │
# │   │  ┌─────────────────────────────────────────┐    │   │
# │   │  │  WHAT YOU DON'T SEE (Hidden)            │    │   │
# │   │  │  • Engine combustion process            │    │   │
# │   │  │  • Fuel injection system                │    │   │
# │   │  │  • Transmission mechanism               │    │   │
# │   │  │  • ECU programming                      │    │   │
# │   │  └─────────────────────────────────────────┘    │   │
# │   └─────────────────────────────────────────────────┘   │
# └─────────────────────────────────────────────────────────┘

# ┌─────────────────────────────────────┐
#                             │           OBJECT-ORIENTED           │
#                             │           PROGRAMMING (OOP)          │
#                             └─────────────────────────────────────┘
#                                               │
#         ┌─────────────────┬─────────────────┼─────────────────┬─────────────────┐
#         ▼                 ▼                 ▼                 ▼                 ▼
# ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
# │   CLASS &    │  │ ENCAPSULATION│  │ INHERITANCE  │  │ POLYMORPHISM │  │ ABSTRACTION  │
# │    OBJECT    │  │              │  │              │  │              │  │              │
# └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘
#        │                 │                 │                 │                 │
#        ▼                 ▼                 ▼                 ▼                 ▼
# ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
# │ Class =      │  │ Private =    │  │ Single =     │  │ Method       │  │ Abstract     │
# │ Blueprint    │  │ __var        │  │ One parent   │  │ Overriding   │  │ Class (ABC)  │
# │              │  │              │  │              │  │              │  │              │
# │ Object =     │  │ Protected =  │  │ Multi-level =│  │ Duck Typing  │  │ Abstract     │
# │ Instance     │  │ _var         │  │ Grand→Parent→│  │ "If it walks │  │ Method       │
# │              │  │              │  │ Child        │  │ like a duck" │  │ @abstractmethod
# │ Constructor  │  │ Getter/      │  │              │  │              │  │              │
# │ _init_()     │  │ Setter       │  │ Multiple =   │  │ Operator     │  │ Interface    │
# │              │  │ @property    │  │ Two+ parents │  │ Overloading  │  │ (Protocol)   │
# │ self         │  │              │  │              │  │ _add_ etc    │  │              │
# └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘


# ┌─────────────────────────────────────┐
#      │           OBJECT-ORIENTED           │
#      │           PROGRAMMING (OOP)          │
#                             └─────────────────────────────────────┘
#                                               │
#         ┌─────────────────┬─────────────────┼─────────────────┬─────────────────┐
#         ▼                 ▼                 ▼                 ▼                 ▼
# ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
# │   CLASS &    │  │ ENCAPSULATION│  │ INHERITANCE  │  │ POLYMORPHISM │  │ ABSTRACTION  │
# │    OBJECT    │  │              │  │              │  │              │  │              │
# └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘
#        │                 │                 │                 │                 │
#        ▼                 ▼                 ▼                 ▼                 ▼
# ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
# │ Class =      │  │ Private =    │  │ Single =     │  │ Method       │  │ Abstract     │
# │ Blueprint    │  │ __var        │  │ One parent   │  │ Overriding   │  │ Class (ABC)  │
# │              │  │              │  │              │  │              │  │              │
# │ Object =     │  │ Protected =  │  │ Multi-level =│  │ Duck Typing  │  │ Abstract     │
# │ Instance     │  │ _var         │  │ Grand→Parent→│  │ "If it walks │  │ Method       │
# │              │  │              │  │ Child        │  │ like a duck" │  │ @abstractmethod
# │ Constructor  │  │ Getter/      │  │              │  │              │  │              │
# │ __init__()   │  │ Setter       │  │ Multiple =   │  │ Operator     │  │ Interface    │
# │              │  │ @property    │  │ Two+ parents │  │ Overloading  │  │ (Protocol)   │
# │ self         │  │              │  │              │  │ __add__ etc  │  │              │
# └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘


# 1. What is Abstraction?
# ==========================================================

"""
Definition

Abstraction is one of the four pillars of
Object-Oriented Programming (OOP).

Abstraction means

"Hiding the implementation details and showing
only the essential features to the user."

The user only knows WHAT the object does,
not HOW it does it.

Real-Life Examples

✔ ATM Machine
You can withdraw money without knowing how the
ATM works internally.

✔ Car
You drive the car using the steering wheel,
brake, and accelerator without knowing how
the engine works.

✔ Mobile Phone
You make calls and use apps without knowing
how the hardware works internally.
"""

# ==========================================================
# 2. Why Use Abstraction?
# ==========================================================

"""
Why Use Abstraction?

✔ Hide unnecessary implementation details.

✔ Improve code security.

✔ Reduce code complexity.

✔ Make programs easier to use.

✔ Improve code readability.

✔ Useful in large projects.
"""

# ==========================================================
# 3. Advantages of Abstraction
# ==========================================================

"""
Advantages

1. Hides internal implementation.

2. Improves security.

3. Reduces complexity.

4. Easy to maintain.

5. Easy to extend.

6. Makes code reusable.

7. Professional programming style.
"""

# ==========================================================
# 4. Abstract Class
# ==========================================================

"""
Abstract Class

An Abstract Class is a class that cannot
be used to create objects directly.

It is only used as a blueprint
for child classes.

An Abstract Class contains

✔ Abstract Methods

✔ Normal Methods (Optional)

To create an Abstract Class,
Python uses the ABC module.
"""

# ==========================================================
# 5. Abstract Method
# ==========================================================

"""
Abstract Method

An Abstract Method is a method that
has only a declaration.

It does not contain any implementation.

Every child class MUST implement
(Abstract Override) that method.

Otherwise Python will generate an error.
"""

# ==========================================================
# 6. ABC Module
# ==========================================================

"""
ABC stands for

Abstract Base Class

Python provides the ABC module
to create Abstract Classes.

Import Statement

from abc import ABC, abstractmethod

ABC

Used to create an Abstract Class.

abstractmethod

Used to create an Abstract Method.
"""

# Import ABC Module
from abc import ABC, abstractmethod

# ==========================================================
# 7. @abstractmethod Decorator
# ==========================================================

"""
@abstractmethod

This decorator is used before
an Abstract Method.

It tells Python that this method
MUST be implemented by every
child class.
"""

# ==========================================================
# Example
# ==========================================================

# Create Abstract Class
class Animal(ABC):

    # Create Abstract Method
    @abstractmethod
    def sound(self):
        pass


# Child Class
class Dog(Animal):

    # Override Abstract Method
    def sound(self):

        print("Dog says Bark Bark")


# Child Class
class Cat(Animal):

    # Override Abstract Method
    def sound(self):

        print("Cat says Meow Meow")


# Create Objects
dog = Dog()

cat = Cat()

# Call Methods
dog.sound()

cat.sound()

# ==========================================================
# 8. Difference Between Abstraction and Encapsulation
# ==========================================================

"""
Abstraction

✔ Hides implementation.

✔ Focuses on WHAT an object does.

✔ Achieved using Abstract Class.

✔ Improves simplicity.

------------------------------------

Encapsulation

✔ Hides data.

✔ Focuses on HOW data is protected.

✔ Achieved using Private Variables.

✔ Improves security.
"""

# ==========================================================
# 9. Simple Abstraction Example
# ==========================================================

print("\n========== Simple Abstraction Example ==========\n")

# Abstract Class
class Shape(ABC):

    # Abstract Method
    @abstractmethod
    def area(self):
        pass


# Child Class
class Rectangle(Shape):

    # Constructor
    def __init__(self, length, width):

        self.length = length
        self.width = width

    # Override Abstract Method
    def area(self):

        return self.length * self.width


# Child Class
class Square(Shape):

    # Constructor
    def __init__(self, side):

        self.side = side

    # Override Abstract Method
    def area(self):

        return self.side * self.side


# Create Objects
rectangle = Rectangle(10, 5)

square = Square(4)

# Call Methods
print("Rectangle Area :", rectangle.area())

print("Square Area :", square.area())
# ==========================================================
# Project 1 : Payment Gateway System
# ==========================================================

"""
Problem Statement

Create a Payment Gateway System.

Requirements

1. Create an Abstract Class Payment.

2. Create an Abstract Method pay().

3. Create Child Classes

   • CreditCard
   • PayPal
   • JazzCash

4. Override pay() in every Child Class.

5. Create Objects and process payments.
"""

# Import ABC Module
from abc import ABC, abstractmethod


# ==========================================================
# Abstract Class
# ==========================================================

class Payment(ABC):

    # Abstract Method
    @abstractmethod
    def pay(self, amount):
        pass


# ==========================================================
# Child Class : CreditCard
# ==========================================================

class CreditCard(Payment):      # Inherit Abstract Class

    # Override Abstract Method
    def pay(self, amount):

        print(f"Paid Rs.{amount} using Credit Card")


# ==========================================================
# Child Class : PayPal
# ==========================================================

class PayPal(Payment):          # Inherit Abstract Class

    # Override Abstract Method
    def pay(self, amount):

        print(f"Paid Rs.{amount} using PayPal")


# ==========================================================
# Child Class : JazzCash
# ==========================================================

class JazzCash(Payment):        # Inherit Abstract Class

    # Override Abstract Method
    def pay(self, amount):

        print(f"Paid Rs.{amount} using JazzCash")


# ==========================================================
# Create Objects
# ==========================================================

credit = CreditCard()       # CreditCard Object

paypal = PayPal()           # PayPal Object

jazz = JazzCash()           # JazzCash Object


# ==========================================================
# Call Methods
# ==========================================================

credit.pay(5000)

paypal.pay(2500)

jazz.pay(1000)



# ==========================================================
# Project 2 : Vehicle Management System
# ==========================================================

"""
Problem Statement

Create a Vehicle Management System.

Requirements

1. Create an Abstract Class Vehicle.

2. Create Abstract Methods

   • start()

   • stop()

3. Create Child Classes

   • Car
   • Bike
   • Bus

4. Override all methods.

5. Create Objects and test the program.
"""


# ==========================================================
# Abstract Class
# ==========================================================

class Vehicle(ABC):

    # Abstract Method
    @abstractmethod
    def start(self):
        pass

    # Abstract Method
    @abstractmethod
    def stop(self):
        pass


# ==========================================================
# Child Class : Car
# ==========================================================

class Car(Vehicle):     # Inherit Abstract Class

    # Override start()
    def start(self):

        print("Car Started")

    # Override stop()
    def stop(self):

        print("Car Stopped")


# ==========================================================
# Child Class : Bike
# ==========================================================

class Bike(Vehicle):    # Inherit Abstract Class

    # Override start()
    def start(self):

        print("Bike Started")

    # Override stop()
    def stop(self):

        print("Bike Stopped")


# ==========================================================
# Child Class : Bus
# ==========================================================

class Bus(Vehicle):     # Inherit Abstract Class

    # Override start()
    def start(self):

        print("Bus Started")

    # Override stop()
    def stop(self):

        print("Bus Stopped")


# ==========================================================
# Create Objects
# ==========================================================

car = Car()         # Car Object

bike = Bike()       # Bike Object

bus = Bus()         # Bus Object


# ==========================================================
# Call Methods
# ==========================================================

car.start()
car.stop()

print()

bike.start()
bike.stop()

print()

bus.start()
bus.stop()

