# ==========================================================
#            Python OOP - Inheritance

# 1. What is Inheritance?
# ==========================================================

"""
Definition

Inheritance is one of the four pillars of
Object-Oriented Programming (OOP).

Inheritance means:

"One class acquires the properties and methods
of another class."

The class that gives properties is called
the Parent (Base) Class.

The class that receives properties is called
the Child (Derived) Class.

Inheritance helps us reuse code instead of
writing the same code again.
"""

# ==========================================================
# 2. Why Use Inheritance?
# ==========================================================

"""
Why Use Inheritance?

✔ Code Reusability

✔ Reduce Duplicate Code

✔ Easy Maintenance

✔ Improves Readability

✔ Creates Parent-Child Relationship

✔ Makes Large Projects Easy to Manage
"""

# ==========================================================
# 3. Advantages of Inheritance
# ==========================================================

"""
Advantages

1. Reuse Existing Code

2. Save Development Time

3. Reduce Code Duplication

4. Easy to Extend Programs

5. Better Code Organization

6. Supports Method Overriding

7. Easy Maintenance
"""

# ==========================================================
# 4. Parent Class
# ==========================================================

"""
Parent Class

A Parent Class is the class whose
properties and methods are inherited
by another class.

It is also called:

✔ Base Class

✔ Super Class
"""

# ==========================================================
# 5. Child Class
# ==========================================================

"""
Child Class

A Child Class inherits the properties
and methods of the Parent Class.

It can also add its own
variables and methods.

It is also called:

✔ Derived Class

✔ Sub Class
"""

# ==========================================================
# Simple Parent and Child Example
# ==========================================================

# Parent Class
class Animal:

    # Parent Method
    def speak(self):

        print("Animal Speaks")


# Child Class
class Dog(Animal):

    # Child Method
    def bark(self):

        print("Dog Barks")


# Create Object
dog = Dog()

# Parent Method
dog.speak()

# Child Method
dog.bark()

"""
Explanation

Dog class inherits Animal class.

Dog object can use

✔ speak()  → Parent Method

✔ bark()   → Child Method
"""

# ==========================================================
# 6. Types of Inheritance
# ==========================================================

"""
Python supports five types of Inheritance.

1. Single Inheritance

2. Multiple Inheritance

3. Multilevel Inheritance

4. Hierarchical Inheritance

5. Hybrid Inheritance (Concept)
"""

# ----------------------------------------------------------
# Single Inheritance
# ----------------------------------------------------------

"""
One Parent Class

↓

One Child Class
"""

class A:
    pass

class B(A):
    pass

print("Single Inheritance")


# ----------------------------------------------------------
# Multiple Inheritance
# ----------------------------------------------------------

"""
Two Parent Classes

↓

One Child Class
"""

class Father:
    pass

class Mother:
    pass

class Child(Father, Mother):
    pass

print("Multiple Inheritance")


# ----------------------------------------------------------
# Multilevel Inheritance
# ----------------------------------------------------------

"""
Grand Parent

↓

Parent

↓

Child
"""

class GrandParent:
    pass

class Parent(GrandParent):
    pass

class Son(Parent):
    pass

print("Multilevel Inheritance")


# ----------------------------------------------------------
# Hierarchical Inheritance
# ----------------------------------------------------------

"""
One Parent

↓

Many Child Classes
"""

class Person:
    pass

class Teacher(Person):
    pass

class Student(Person):
    pass

print("Hierarchical Inheritance")


# ----------------------------------------------------------
# Hybrid Inheritance
# ----------------------------------------------------------

"""
Hybrid Inheritance

Combination of two or more
types of inheritance.

Python supports Hybrid
Inheritance.
"""

# ==========================================================
# 7. super() Function
# ==========================================================

"""
super()

The super() function is used to
call the Parent Class constructor
or methods.

It avoids rewriting Parent Class code.
"""

# Parent Class
class Person:

    def __init__(self, name):

        self.name = name


# Child Class
class Student(Person):

    def __init__(self, name, roll_no):

        # Call Parent Constructor
        super().__init__(name)

        self.roll_no = roll_no

    def display(self):

        print("Name :", self.name)

        print("Roll No :", self.roll_no)


# Object
s = Student("Eisha", 101)

s.display()


# ==========================================================
# Method Overriding
# ==========================================================

"""
Method Overriding

When a Child Class creates
its own version of a Parent
Class method.

The Child Method replaces
the Parent Method.
"""

# Parent Class
class Bird:

    def sound(self):

        print("Bird Sound")


# Child Class
class Sparrow(Bird):

    # Override Parent Method
    def sound(self):

        print("Sparrow Chirps")


# Object
b = Sparrow()

b.sound()

# ==========================================================
# Project 1 : Vehicle Management System
# ==========================================================

"""
Problem Statement

Create a Vehicle Management System using Inheritance.

Requirements

1. Create a Parent Class Vehicle.

2. Add Attributes:
   - brand
   - model
   - year

3. Add Methods:
   - start()
   - stop()
   - display_info()

4. Create Child Class Car.
   - doors
   - fuel_type
   - honk()

5. Create Child Class Bike.
   - engine_cc
   - has_gear
   - ring_bell()

6. Create Child Class ElectricCar from Car.
   - battery_capacity
   - charge()

7. Use super() constructor.

8. Override display_info().

9. Create Objects and test all methods.

10. Display Method Resolution Order (MRO).
"""

# ==========================================================
# Parent Class
# ==========================================================

class Vehicle:

    # Parent Constructor
    def __init__(self, brand, model, year):

        self.brand = brand
        self.model = model
        self.year = year

    # Parent Method
    def start(self):

        print(f"{self.brand} {self.model} is Starting...")

    # Parent Method
    def stop(self):

        print(f"{self.brand} {self.model} is Stopping...")

    # Parent Method
    def display_info(self):

        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Year  : {self.year}")


# ==========================================================
# Child Class : Car
# ==========================================================

class Car(Vehicle):

    # Child Constructor
    def __init__(self, brand, model, year, doors, fuel_type):

        # Call Parent Constructor
        super().__init__(brand, model, year)

        self.doors = doors
        self.fuel_type = fuel_type

    # Child Method
    def honk(self):

        print("Beep Beep!")

    # Method Overriding
    def display_info(self):

        # Parent Method Call
        super().display_info()

        print(f"Doors : {self.doors}")
        print(f"Fuel  : {self.fuel_type}")


# ==========================================================
# Child Class : Bike
# ==========================================================

class Bike(Vehicle):

    # Child Constructor
    def __init__(self, brand, model, year, engine_cc, has_gear):

        # Parent Constructor Call
        super().__init__(brand, model, year)

        self.engine_cc = engine_cc
        self.has_gear = has_gear

    # Child Method
    def ring_bell(self):

        print("Ding Dong!")

    # Method Overriding
    def display_info(self):

        super().display_info()

        print(f"Engine CC : {self.engine_cc}")
        print(f"Gear      : {self.has_gear}")


# ==========================================================
# Child Class : ElectricCar
# ==========================================================

class ElectricCar(Car):

    # Child Constructor
    def __init__(self, brand, model, year, doors, fuel_type, battery_capacity):

        # Call Car Constructor
        super().__init__(brand, model, year, doors, fuel_type)

        self.battery_capacity = battery_capacity

    # Child Method
    def charge(self):

        print(f"{self.brand} is Charging...")

    # Method Overriding
    def display_info(self):

        # Call Parent Method
        super().display_info()

        print(f"Battery : {self.battery_capacity} kWh")


# ==========================================================
# Create Objects
# ==========================================================

car = Car("Toyota", "Corolla", 2024, 4, "Petrol")

bike = Bike("Honda", "CG125", 2023, 125, True)

electric = ElectricCar("Tesla", "Model S", 2025, 4, "Electric", 100)


# ==========================================================
# Call Methods
# ==========================================================

print("========== Car ==========")

car.display_info()
car.start()
car.honk()
car.stop()

print("\n========== Bike ==========")

bike.display_info()
bike.start()
bike.ring_bell()
bike.stop()

print("\n========== Electric Car ==========")

electric.display_info()
electric.start()
electric.charge()
electric.stop()


# ==========================================================
# Method Resolution Order (MRO)
# ==========================================================

print("\nCar MRO")
print(Car.mro())

print("\nBike MRO")
print(Bike.mro())

print("\nElectricCar MRO")
print(ElectricCar.mro())



# ==========================================================
# Project 2 : Employee Payroll System
# ==========================================================

"""
Problem Statement

Create an Employee Payroll System using Inheritance.

Requirements

1. Create Parent Class Employee.

2. Add Attributes:
   - name
   - employee_id
   - base_salary

3. Add Method:
   - calculate_salary()

4. Create Child Class HourlyEmployee.
   - hourly_rate
   - hours_worked

5. Create Child Class SalariedEmployee.
   - annual_salary
   - bonus

6. Create Child Class CommissionEmployee
   inherited from SalariedEmployee.

7. Add:
   - commission_rate
   - sales

8. Override calculate_salary().

9. Create Objects.

10. Display salary of every employee.
"""


# ==========================================================
# Parent Class
# ==========================================================

class Employee:

    # Parent Constructor
    def __init__(self, name, employee_id, base_salary):

        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    # Parent Method
    def calculate_salary(self):

        return self.base_salary

    # Parent Method
    def display(self):

        print(f"Name : {self.name}")
        print(f"Employee ID : {self.employee_id}")


# ==========================================================
# Child Class : HourlyEmployee
# ==========================================================

class HourlyEmployee(Employee):

    def __init__(self, name, employee_id, hourly_rate, hours_worked):

        # Call Parent Constructor
        super().__init__(name, employee_id, 0)

        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    # Method Overriding
    def calculate_salary(self):

        return self.hourly_rate * self.hours_worked


# ==========================================================
# Child Class : SalariedEmployee
# ==========================================================

class SalariedEmployee(Employee):

    def __init__(self, name, employee_id, annual_salary, bonus):

        # Call Parent Constructor
        super().__init__(name, employee_id, annual_salary)

        self.annual_salary = annual_salary
        self.bonus = bonus

    # Method Overriding
    def calculate_salary(self):

        return self.annual_salary + self.bonus


# ==========================================================
# Child Class : CommissionEmployee
# ==========================================================

class CommissionEmployee(SalariedEmployee):

    def __init__(self, name, employee_id, annual_salary, bonus,
                 commission_rate, sales):

        # Call Parent Constructor
        super().__init__(name, employee_id, annual_salary, bonus)

        self.commission_rate = commission_rate
        self.sales = sales

    # Method Overriding
    def calculate_salary(self):

        commission = self.sales * self.commission_rate

        return self.annual_salary + self.bonus + commission


# ==========================================================
# Create Objects
# ==========================================================

hourly = HourlyEmployee("Eisha", 101, 500, 8)

salary = SalariedEmployee("Ayesha", 102, 60000, 10000)

commission = CommissionEmployee(
    "Zahra",
    103,
    80000,
    15000,
    0.10,
    50000
)


# ==========================================================
# Display Results
# ==========================================================

print("\n========== Hourly Employee ==========")

hourly.display()

print("Salary :", hourly.calculate_salary())

print("\n========== Salaried Employee ==========")

salary.display()

print("Salary :", salary.calculate_salary())

print("\n========== Commission Employee ==========")

commission.display()

print("Salary :", commission.calculate_salary())

# ==========================================================
# Project 3 : Student Management System
# ==========================================================

"""
Problem Statement

Create a Student Management System using Inheritance.

Requirements

1. Create Parent Class Person.

2. Add Attributes:
   - name
   - age

3. Add Method:
   - display_person()

4. Create Child Class Student.

5. Add Attributes:
   - roll_no
   - marks

6. Add Method:
   - display_student()

7. Use super() constructor.

8. Create Object and display student information.
"""

# ==========================================================
# Parent Class
# ==========================================================

class Person:

    # Parent Constructor
    def __init__(self, name, age):

        self.name = name
        self.age = age

    # Parent Method
    def display_person(self):

        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


# ==========================================================
# Child Class
# ==========================================================

class Student(Person):

    # Child Constructor
    def __init__(self, name, age, roll_no, marks):

        # Call Parent Constructor
        super().__init__(name, age)

        self.roll_no = roll_no
        self.marks = marks

    # Child Method
    def display_student(self):

        # Call Parent Method
        super().display_person()

        print(f"Roll No : {self.roll_no}")
        print(f"Marks   : {self.marks}")


# ==========================================================
# Create Object
# ==========================================================

student = Student("Eisha", 21, 101, 95)

student.display_student()



# ==========================================================
# Project 4 : Animal Management System
# ==========================================================

"""
Problem Statement

Create an Animal Management System using Inheritance.

Requirements

1. Create Parent Class Animal.

2. Add Method:
   - sound()

3. Create Child Classes:
   - Dog
   - Cat
   - Cow

4. Override sound() method.

5. Create Objects and test the program.
"""

# ==========================================================
# Parent Class
# ==========================================================

class Animal:

    # Parent Method
    def sound(self):

        print("Animals make different sounds.")


# ==========================================================
# Child Class : Dog
# ==========================================================

class Dog(Animal):

    # Method Overriding
    def sound(self):

        print("Dog Says : Bark Bark")


# ==========================================================
# Child Class : Cat
# ==========================================================

class Cat(Animal):

    # Method Overriding
    def sound(self):

        print("Cat Says : Meow Meow")


# ==========================================================
# Child Class : Cow
# ==========================================================

class Cow(Animal):

    # Method Overriding
    def sound(self):

        print("Cow Says : Moo Moo")


# ==========================================================
# Create Objects
# ==========================================================

dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
cat.sound()
cow.sound()



# ==========================================================
# Project 5 : Bank Management System
# ==========================================================

"""
Problem Statement

Create a Bank Management System using Inheritance.

Requirements

1. Create Parent Class BankAccount.

2. Add Attributes:
   - account_number
   - balance

3. Add Methods:
   - deposit()
   - withdraw()
   - display_balance()

4. Create Child Class SavingAccount.

5. Create Child Class CurrentAccount.

6. Use Inheritance.

7. Create Objects and test the program.
"""

# ==========================================================
# Parent Class
# ==========================================================

class BankAccount:

    # Parent Constructor
    def __init__(self, account_number, balance):

        self.account_number = account_number
        self.balance = balance

    # Deposit Method
    def deposit(self, amount):

        self.balance += amount

        print(f"Deposited : {amount}")

    # Withdraw Method
    def withdraw(self, amount):

        if amount <= self.balance:

            self.balance -= amount

            print(f"Withdraw : {amount}")

        else:

            print("Insufficient Balance")

    # Display Method
    def display_balance(self):

        print(f"Current Balance : {self.balance}")


# ==========================================================
# Child Class : SavingAccount
# ==========================================================

class SavingAccount(BankAccount):

    # Child Method
    def interest(self):

        print("Saving Account earns Interest.")


# ==========================================================
# Child Class : CurrentAccount
# ==========================================================

class CurrentAccount(BankAccount):

    # Child Method
    def overdraft(self):

        print("Current Account provides Overdraft Facility.")


# ==========================================================
# Create Objects
# ==========================================================

saving = SavingAccount("SA101", 50000)

current = CurrentAccount("CA201", 75000)


# ==========================================================
# Test Saving Account
# ==========================================================

saving.deposit(5000)

saving.withdraw(2000)

saving.display_balance()

saving.interest()


print()


# ==========================================================
# Test Current Account
# ==========================================================

current.deposit(10000)

current.withdraw(15000)

current.display_balance()

current.overdraft()