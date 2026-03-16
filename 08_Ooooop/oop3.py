

class Dog:
    # class variables: shared by all instances.
    species = "Canis lupus familaries"

    # __init__ is the constructor - runs when you create an instance
    def __init__(self, name:str, breed: str, age: int):
        # instance variable- unique to each object
        self.name = name 
        self.breed = breed
        self.age = age 

    # instance methods: operate on the specific object. 
    def bark(self) -> str:
        return f"{self.name} says: Woof!"

    def is_senior(self) -> str:
        return self.age >= 8

    # __repr__ - what developers seee(in debugger, logs, REPL)
    def __repr__(self) -> str:
        return f"Dog(name={self.name!r}, breed={self.breed!r}, age={self.age})"


    # __str__ - what end users see (print(), str())
    def __str__(self)-> str:
        return f"{self.name} the {self.breed}"
    

# Creating the instances. 
dog1 = Dog("Rex", "German Shepherd", 3)   
dog2 = Dog("Bella", "Labrador", 9) 

print(dog1)  # <-  __str__
print(repr(dog1))
print(dog1.bark())
print(dog2.is_senior())

# Class variable is shared
print(dog1.species)      # Canis lupus familiaris
print(dog2.species)      # Canis lupus familiaris
print(Dog.species)       # same — accessed from class directly

# Instance variables are separate
print(dog1.name)         # Rex
print(dog2.name)         # Bella


# under the hood when we all dog1.bark(), python 
# actually calls Dog.bark(dog1) - self is instance passed automatically.

