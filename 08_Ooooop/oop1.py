
# 🔹 What is OOP?
# Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure code.
#  The key concepts in OOP are:

# Classes - Blueprints for creating objects (instances).
# Objects - Instances of classes.
# Methods - Functions defined inside a class.
# Attributes - Variables defined inside a class.

# ✅ Defining a Class
class Dog:
    def __init__(self, name, age):
        self.name = name 
        self.age = age  
    
    def bark(self):
        return f"{self.name} is barking!!"

# ✅ Creating an Object
dog1 = Dog("Tony", 3)
# print(dog1.age)
# print(dog1.name)
# print(dog1.bark())

# 🔹 2. __init__ Method (Constructor)
# The __init__ method is a special method that is automatically called when an object is created. 
# It's used to initialize the object's attributes with values when the object is created.

# Create a class called Person with attributes name and age.
# Add a method introduce that prints a message like: "Hi, my name is [name] and I'm [age] years old."
# Create an instance of the Person class and call the introduce method
# 

class Person:
    profession = "student"  # class variable..
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def introduce(self):
        return f"Hi, my name is {self.name} and I'm {self.age} years old."
    
    def __str__(self): # helps in printing our whole instance otherwise it will print address!!!
        return f"{self.name} ,{self.age}"
    
person1 = Person("Roy", 22)
# print(person1) 

# print(person1.profession)
# print(Person.profession)
# print(person1.introduce())


# 🔹 3. Instance Variables vs. Class Variables
# Instance Variables: These are variables that belong to the specific instance (object) of the class. Each object can have its own instance variables.
# Class Variables: These are variables that belong to the class itself, and all instances of the class share the same class variable.

