# Chapter 14: Object-Oriented Programming (OOP) Basics

"""
Introduction:
Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to model real-world entities. This chapter introduces the basic concepts of OOP, including classes, objects, methods, and attributes.

Key Concepts:
1. Classes: Templates for creating objects, defining methods and attributes.
2. Objects: Instances of a class.
3. Methods: Functions defined within a class that define the behavior of the objects.
4. Attributes: Variables that hold the state of an object.

Notes:
- A class is a blueprint for creating objects (instances).
- Methods are functions that belong to a class and define behaviors.
- Attributes are characteristics or properties of an object.

"""

# Program: Create a BankAccount class with deposit and withdraw methods

class BankAccount:
    """
    A class representing a bank account.

    Attributes:
        owner (str): The name of the account holder.
        balance (float): The current balance in the account.
    """

    def __init__(self, owner, balance=0):
        """
        Initialize a new bank account.

        Parameters:
            owner (str): The name of the account holder.
            balance (float): The initial balance (default is 0).
        """
        self.owner = owner  # Attribute to store the owner's name
        self.balance = balance  # Attribute to store the account balance

    def deposit(self, amount):
        """
        Deposit money into the account.

        Parameters:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Parameters:
            amount (float): The amount to withdraw.
        """
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdraw amount must be positive.")

    def display_balance(self):
        """Display the current balance of the account."""
        print(f"Current balance: {self.balance}")


# Create an instance (object) of the BankAccount class
account = BankAccount("Alice", 1000)

# Display initial balance
account.display_balance()

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(200)

# Try withdrawing more than the available balance
account.withdraw(1500)

# Display final balance
account.display_balance()
