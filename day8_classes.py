# Day 8: Classes & Objects

print("=== Your First Class ===")
print()

# Define a class
class Dog:
    """A simple Dog class"""
    
    # Class attribute (shared by all dogs)
    species = "Canis familiaris"
    
    # Constructor - runs when creating a new dog
    def __init__(self, name, age):
        """Initialize a new dog"""
        self.name = name    # Instance attribute (unique to each dog)
        self.age = age      # Instance attribute
    
    # Method - what a dog can do
    def bark(self):
        """Make the dog bark"""
        print(f"{self.name} says Woof!")
    
    def description(self):
        """Return description of the dog"""
        return f"{self.name} is {self.age} years old"


# Create objects (instances of the Dog class)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Access attributes
print(f"Dog 1: {dog1.name}, Age: {dog1.age}")
print(f"Dog 2: {dog2.name}, Age: {dog2.age}")

# Call methods
dog1.bark()
dog2.bark()

print(dog1.description())
print(dog2.description())

# Access class attribute
print(f"All dogs are: {Dog.species}")


# Understanding 'self'

print("\n=== Understanding self ===")
print()

class Person:
    def __init__(self, name, age):
        # self refers to THIS specific person object
        self.name = name
        self.age = age
    
    def introduce(self):
        # self lets us access THIS person's attributes
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")
    
    def have_birthday(self):
        # self lets us modify THIS person's attributes
        self.age += 1
        print(f"Happy birthday! {self.name} is now {self.age}")


# Create two different people
alice = Person("Alice", 25)
bob = Person("Bob", 30)

# Each object has its own data
alice.introduce()  # Uses alice's name and age
bob.introduce()    # Uses bob's name and age

# Methods affect only the specific object
alice.have_birthday()  # Only alice's age increases
alice.introduce()      # Alice is now 26
bob.introduce()        # Bob is still 30




# Practical Example: Bank Account

print("\n=== Bank Account Example ===")
print()

class BankAccount:
    """A simple bank account class"""
    
    def __init__(self, owner, balance=0):
        """Create a new account"""
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Add money to account"""
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("❌ Deposit amount must be positive!")
    
    def withdraw(self, amount):
        """Take money from account"""
        if amount > self.balance:
            print(f"❌ Insufficient funds! Balance: ${self.balance}")
        elif amount <= 0:
            print("❌ Withdrawal amount must be positive!")
        else:
            self.balance -= amount
            print(f"✅ Withdrew ${amount}. New balance: ${self.balance}")
    
    def get_balance(self):
        """Check current balance"""
        return self.balance
    
    def __str__(self):
        """String representation of account"""
        return f"Account({self.owner}, Balance: ${self.balance})"


# Create accounts
alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob", 500)

print(alice_account)
print(bob_account)

# Use the accounts
alice_account.deposit(500)
alice_account.withdraw(200)
print(f"Alice's balance: ${alice_account.get_balance()}")

bob_account.withdraw(600)  # Not enough money!
bob_account.deposit(200)
bob_account.withdraw(600)  # Now it works
print(f"Bob's balance: ${bob_account.get_balance()}")

# Class Attributes vs Instance Attributes

print("\n=== Class vs Instance Attributes ===")
print()

class Employee:
    company = "TechCorp"
    employee_count = 0
    
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        Employee.employee_count += 1
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")
        print(f"Company: {self.company}")
        print()


emp1 = Employee("Alice", "Developer", 80000)
emp2 = Employee("Bob", "Designer", 70000)
emp3 = Employee("Charlie", "Manager", 90000)

emp1.display_info()
emp2.display_info()

print(f"All work at: {Employee.company}")
print(f"Total employees: {Employee.employee_count}")

Employee.company = "NewTech Corp"
print(f"\nAfter company name change:")
print(f"emp1 company: {emp1.company}")
print(f"emp2 company: {emp2.company}")
print(f"emp3 company: {emp3.company}")

# Special Methods (Magic Methods)

print("\n=== Special Methods ===")
print()

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"
    
    def __eq__(self, other):
        return self.width == other.width and self.height == other.height
    
    def __add__(self, other):
        total_area = self.area() + other.area()
        return f"Combined area: {total_area}"


rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)
rect3 = Rectangle(5, 10)

print(rect1)
print(f"Area: {rect1.area()}")
print(f"Perimeter: {rect1.perimeter()}")
print(f"rect1 == rect2: {rect1 == rect2}")
print(f"rect1 == rect3: {rect1 == rect3}")
print(rect1 + rect2)